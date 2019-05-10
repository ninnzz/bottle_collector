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

    # SOMETHING LIKE THIS
    # You need to figure out where to get the values needed here
    # User({
    #     'id': None, # new items always have NONE IDS
    #     'name': '',
    #     'contact_number': '',
    #     'address': '',
    #     'birthday': datetime.now(),
    #     'gender': ''        
    # })

    return