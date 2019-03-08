from db import db
import datetime


class BaseModel(db.Model):
    __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models

    # Navodno bi sve ostale klase terbale nasljedivat od ove!


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    full_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))
    active = db.Column(db.Boolean, default=True)
    role = db.Column(db.Integer, default=3)
    user_details = db.relationship("UserDetails", backref="user")

    def __init__(self,first_name, last_name, full_name, email, password, active, role):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.password = password
        self.active = active
        self.role = role


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_full_name(cls, full_name):
        return cls.query.filter_by(full_name=full_name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(femail=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    postal_code = db.Column(db.String(50))
    birth_date = db.Date()
    gender = db.Column(db.String(1))    # samo m/f ?
    avatar = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, adress, phone_number, postal_code, birth_date, gender, avatar, created_at, updated_at):
        self.adress = adress
        self.phone_number = phone_number
        self.postal_code = postal_code
        self.birth_date = birth_date
        self.gender = gender
        self.avatar = avatar
        self.created_at = created_at
        self.updated_at = updated_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

