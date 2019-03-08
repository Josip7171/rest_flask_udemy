import sqlite3
from db import db


# ovaj UserModel je API! (nije rest)
# sastoji se od 2 API endpoint methods find_by_username i by_id
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    user_info = db.relationship('UserInfoModel')

    def json(self):
        return {
            'name': self.username,
            'user id': self.id,
            'user info': [info.json() for info in self.user_info]
        }


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


