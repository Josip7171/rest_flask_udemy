from db import db
import datetime


class UserInfoModel(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    full_name = db.Column(db.String(50))
    adress = db.Column(db.String(40))
    postal_code = db.Column(db.Integer)
    phone_number = db.Column(db.String(15))
    birth_date = db.Column(db.String(10))
    gender = db.Column(db.String(6))
    avatar = db.Column(db.String(25))
    active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(10))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, user_id, first_name, last_name, full_name, adress, postal_code, phone_number,
                 birth_date, gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.adress = adress
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.gender = gender
        self.avatar = ""
        self.role = "User"
        self.created_at = str(datetime.datetime.utcnow())
        self.updated_at = str(datetime.datetime.utcnow())


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'adress': self.adress,
            'postal_code': self.postal_code,
            'phone_number': self.phone_number,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'avatar': self.avatar,
            'role': self.role,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()




