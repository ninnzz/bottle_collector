"""
Define all routes here
"""
from models import *
from models import db
from flask import request
from config import Config
from flask import Blueprint
from datetime import datetime
from predictor import classifier
from camera_library import vid_worker
from flask import Flask, make_response
from mfrc522 import SimpleMFRC522
from flask import render_template, Response, send_from_directory, jsonify
from gevent import queue, spawn, monkey

import os
import cv2
import time
import json
# import queue
import random
import numpy as np
import RPi.GPIO as GPIO


monkey.patch_all()
body = queue.Queue()
handler = Blueprint('router', __name__)

@handler.route('/')
def index():
    resp = make_response(render_template('page2.html',**locals()))
    resp.set_cookie('user_id', user_id)
    print(resp)
    return resp 


@handler.route('/get_rfid_info', methods=['GET'])
def get_rfid():
    reader = SimpleMFRC522()

    try:
        id, text = reader.read()
        user = db.session.query(User).filter(User.rfid == id).first()
        
    finally:
        GPIO.cleanup()

    return Response(json.dumps({'id': user.id}), headers={'Content-Type':'application/json'})


@handler.route('/get_user', methods=['POST'])
def sample_route():
    user_id = request.form['user_id']
    user = db.session.query(User).filter(User.id == user_id).first()
    
    if user is None:
        return "Error"

    transactions = db.session.query(Transaction, Bottle) \
        .join(Bottle, Bottle.id == Transaction.bottle_type) \
        .filter(Transaction.user_id  == user.id).all()

    name = user.name
    address = user.address
    birthday = user.birthday
    gender = user.gender

    _tr = []
    total_points = 0

    for tr in transactions:
        _tr.append({
            'location_id': tr.Transaction.location_id,
            'bottle_name': tr.Bottle.name,
            'date': tr.Transaction.date.strftime('%Y-%m-%d'),
            'points': tr.Bottle.points   
        })

        total_points += tr.Bottle.points

    username = request.cookies.get('user_id')
    resp = make_response(render_template('page2.html',**locals()))
    resp.set_cookie('user_id', user_id)
    return resp

@handler.route('/check_prices', methods=['POST'])
def check_prices():

    bottle = None

    def on_img(data):
        result = classifier.predict(data)
        if len(result) > 0:
            return result[0]
        return None

    vid_worker.on_img = on_img
    vid_worker.screenshot = True

    while(True):
        if vid_worker.bottle_result is not None:
            bottle = vid_worker.bottle_result
            vid_worker.bottle_result = None
            break
        time.sleep(0.1)

    bottle_lookup = db.session.query(Bottle).filter(Bottle.name == bottle).first()

    bottle_id= {
                    'id' : bottle_lookup.type,
                    'name' : bottle_lookup.name,
                    'points' : bottle_lookup.points,
                }
    return Response(json.dumps(bottle_id), headers={'Content-Type':'application/json'})

@handler.route('/add_users', methods=['POST'])
def add_user():
    user = User    ({
        'id': None,
        'name': '',
        'address': '',
        'birthday': '',
        'gender' : ''        
        })

    return bottles.serialize()

@handler.route('/stream')
def stream():
    boundary = 'app'

    def on_vid(data):

        rc, data = cv2.imencode('.jpg', data)

        out = '--{}\n'.format(boundary).encode()
        out += b'Content-type: image/jpeg\n'
        out += 'Content-length: {}\n'.format(len(data)).encode()
        out += b'\n'
        out += data.tostring()
        out += b'\n'
        global body
        body.put(out)

    def on_end():
        body.put_nowait(StopIteration)

    # def gen():
    #     while True:
    #         yield body.get()
        

    vid_worker.on_vid = on_vid
    vid_worker.on_end = on_end
    spawn(vid_worker.start)
    # vid_worker.start()

    return Response(body,
                    mimetype='multipart/x-mixed-replace; boundary={}'.format(boundary),
                    content_type='multipart/x-mixed-replace; boundary={}'.format(boundary),
                    status='200',
                    headers={
                        'Connection': 'keep-alive',
                        'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate',
                        'Pragma': 'no-cache'
                    })

@handler.route('/submit_bottle_records', methods=['POST'])
def bottle_records():
    user = request.cookies.get('user_id')

    # Change this to get the value from request.form
    bottle_list = request.form['bottle_ids']
    bottle_id = bottle_list.strip(" ")
    bottle_list = bottle_id.split(" ")
    bottle_list = [int(bottle_ids) for bottle_ids in bottle_list]
    location_id = 1

    for bottle_id in bottle_list:
        db.session.add(Transaction({
            'id': None,
            'user_id': user,
            'location_id': location_id ,
            'bottle_type': bottle_id,
            'date': datetime.now()  
            }))

    db.session.commit()

    unique_bottles = list(set(bottle_list))
    bottle_info = db.session.query(Bottle).filter(Bottle.id.in_(unique_bottles)).all()
    
    points_map = {bottle.id: bottle.points for bottle in bottle_info}
    total_points = 0

    for bottle_id in bottle_list:
        total_points += points_map[bottle_id]

    return render_template('page5.html',**locals())


@handler.route('/add_training_image', methods=['POST'])
def add_to_training():

    bottle_name = request.form['bottle_name']
    
    def on_img(data):

        # Check if folder for bottle already exists
        _bottle_folder = os.path.join(Config.IMAGES_FOLDER, bottle_name)
        if(not os.path.isdir(_bottle_folder)):
            os.mkdir(_bottle_folder)

        # Write to file
        _fname = 'i-{}.jpg'.format(time.time())
        _file_path = os.path.join(_bottle_folder, _fname)
        cv2.imwrite(_file_path, data)

        return None

    vid_worker.on_img = on_img
    vid_worker.screenshot = True

    return "ok"

@handler.route('/page1', methods=['GET'])
def scan_page():
    return render_template('page1.html',**locals())

@handler.route('/page2', methods=['GET'])
def profile_page():
    return render_template('page2.html',**locals()) 

@handler.route('/page4', methods=['GET'])
def camera_page():
    return render_template('page4.html',**locals())

@handler.route('/page5', methods=['GET'])
def thankyou_page():
    return render_template('page5.html',**locals())

@handler.route('/training_page', methods=['GET'])
def training_page():
    return render_template('training.html',**locals())

@handler.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('javascript', path)

@handler.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@handler.route('/wasted')
def waste():
    while True:
        a = 1

    return "a"
