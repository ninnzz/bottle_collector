"""
Define all routes here
"""
from models import db
from models import *
from flask import Blueprint
from datetime import datetime


handler = Blueprint('router', __name__)

@handler.route('/hello_user', methods=['GET'])
def sample_route():

    # TODO
    # STUDY HOW "query" works. 
    # STUDY HOW TO FILTER QUERY RESULTS
    first_user = db.session.query(User).first()
    return first_user.name

# TODO
# ADD THE NEEDED ROUTES

@handler.route('/add_user', methods=['POST'])
def add_user():
    user = User({
       'id': None,
        'name': '',
        'address': '',
        'birthday': datetime.now(),
        'gender': ''        
     })

    db.session.add(user)
    db.session.commit()

    return user.serialize()

@handler.route('/add_bottles', methods=['POST'])
def add_bottle():
    Bottle({
        'id': None,
        'name': '',
        'type': '',
        'points': ''        
     })

    return Bottle

@handler.route('/add_location', methods=['POST'])
def add_location():
    Location({
        'id': None,
        'location_name': ''      
     })

    return Location

@handler.route('/add_transactions', methods=['POST'])
def add_transaction():
    Transaction({
        'id': None,
        'user_name': '',
        'location_id': '',
        'bottle_type':'',
        'date': datetime.now()       
     })

    return Transaction

