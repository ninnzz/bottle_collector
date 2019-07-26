from flask_sqlalchemy import SQLAlchemy

__all__ = ['User', 'Bottle', 'Location','Transaction']

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    rfid = db.Column(db.String(64), default=None)
    name = db.Column(db.String(64), unique=True, nullable=False)
    address = db.Column(db.String(128), default=None)
    birthday = db.Column(db.Date, default=None)
    gender = db.Column(db.String(4), default=None)

    def __init__(self, user_obj):
        self.id = user_obj['id']
        self.rfid = None
        self.name = user_obj['name']
        self.address = user_obj['address']
        self.birthday = user_obj['birthday']
        self.gender = user_obj['gender']

class Bottle(db.Model):
        
    __tablename__ = 'bottles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    

    def __init__(self, bottles_obj):
        self.name = bottles_obj['name']
        self.type = bottles_obj['_type']
        self.points = bottles_obj['points']

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, location_obj):
        self.location_name = location_obj['location_name']

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    location_id = db.Column(db.Integer, default=None)
    bottle_type = db.Column(db.Integer, default=None)
    date = db.Column(db.DateTime(6), default=None)

    def __init__(self, transactions_obj):
        self.user_id = transactions_obj['user_id']
        self.location_id = transactions_obj['location_id']
        self.bottle_type = transactions_obj['bottle_type']
        self.date = transactions_obj['date']
        
        





    
