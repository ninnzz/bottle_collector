""
Define all routes here
"""
from models import db
from models import *
from flask import Blueprint
from datetime import datetime
from flask import Flask, make_response  
from flask import request
from flask import render_template
import random

# to save cookie
import json

# to load cookie
import json




handler = Blueprint('router', __name__)

@handler.route('/')
def index():
    username = request.cookies.get('user_id')
    print( username)
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

    transactions = db.session.query(Transaction).filter(Transaction.user_id  == user.id).all()

    name = user.name
    address = user.address
    birthday = user.birthday
    gender = user.gender

    _tr = []

    for tr in transactions:
        _tr.append({
            'location': tr.location_id,
            'bottle_type': tr.bottle_type,
            'date': tr.date,   
        })
        print(tr.location_id, tr.bottle_type, tr.date)


    username = request.cookies.get('user_id')
    resp = make_response(render_template('page2.html',**locals()))
    resp.set_cookie('user_id', user_id)
    return resp

@handler.route('/check_prices', methods=['GET'])
def check_prices():

    bottles = [
        {
            "bottle_name": "coke",
            "points": 5,
        },

        {
            "bottle_name": "le minerale",
            "points": 10,
        },

        {
            "bottle_name": "sprite",
            "points": 20,
        }
        
    ]

    rand = random.choice(bottles)
    print(rand) 
    return json.dumps(rand)


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
