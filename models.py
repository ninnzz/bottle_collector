from flask_sqlalchemy import SQLAlchemy

__all__ = ['User', 'Bottle']
db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    address = db.Column(db.String(128), default=None)
    birthday = db.Column(db.Date, default=None)
    gender = db.Column(db.String(4), default=None)

    def __init__(self, user_obj):
        self.name = user_obj['name']
        self.address = user_obj['address']
        self.birthday = user_obj['birthday']
        self.gender = user_obj['gender']


class Bottle(db.Model):

    __tablename__ = 'bottle'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    
    def __init__(self, bottles_obj):
        self.name = bottles_obj['name']
        self._type = bottles_obj['_type']
        self.points = bottles_obj['points']

# TODO
# Fill out the rest