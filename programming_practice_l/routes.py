"""
Define all routes here
"""
from models import db
from models import *
from flask import Blueprint
from datetime import datetime
from flask import Flask, make_response  
from flask import request, send_from_directory
from flask import render_template, Response
from camera_library import Video
import pdb
import random

# to save cookie
import json

# to load cookie
import json




handler = Blueprint('router', __name__)

@handler.route('/')
def index():
    resp = make_response(render_template('page2.html',**locals()))
    resp.set_cookie('user_id', user_id)
    print(resp)
    return resp 


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

    #image = request.files[0]
    # image = request.files['file_name']
    # print(image)

    user_id = request.cookies.get('user_id')
    print('USER_ID: ', user_id)

    bottles = [
        {
            "id": 1,
            "bottle_name": "coke",
            "points": 5,
        },

        {
            "id": 2,
            "bottle_name": "royal",
            "points": 5,
        },

        {
            "id": 3,
            "bottle_name": "wilkins",
            "points": 10,
        }
        
    ]

    rand = random.choice(bottles)
    return Response(json.dumps(rand), headers={'Content-Type': 'application/json'})


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

@handler.route('/add_bottles', methods=['POST'])
def add_bottle():
    Bottle({
        'id': None,
        'name': '',
        'type': '',
        'points': ''        
     })

    return bottles.serialize()

@handler.route('/add_location', methods=['POST'])
def add_location():
    Location({
        'id': None,
        'location_name': ''      
     })

    return location.serialize()

@handler.route('/add_transactions', methods=['POST'])
def add_transaction():
    Transaction({
        'id': None,
        'user_id': '',
        'location_id': '',
        'bottle_type':'',
        'date': datetime.now()       
     })

    return transactions.serialize

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

@handler.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('javascript', path)

@handler.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


def gen(capture):
    while True:
        frame = capture.get_frame()
        yield frame

@handler.route('/stream')
def stream():

    boundary = 'app'

    return Response(gen(Video()),
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