from app import db
from datetime import date, datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Integer, default=3)

    def __repr__(self):
        return '<User %r>' % self.full_name


class UserDetail(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    adress = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    postal_code = db.Column(db.String(10))
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(1))
    avatar = db.Column(db.String(25))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    updated_at = db.Column(db.Date, default=date.today)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('user', backref=db.backref('userdetail', lazy=True))


    def __init__(self, created_ad, updated_at, active):
        self.created_at = created_ad
        self.updated_at = updated_at
        self.active = active

        def __repr__(self):
            return '<UserDetail %r>' % self.last_name


