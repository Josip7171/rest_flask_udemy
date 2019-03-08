import sqlite3
from db import db


# ovaj UserModel je API! (nije rest)
# sastoji se od 2 API endpoint methods find_by_username i by_id
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    TABLE_NAME = 'users'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # ovaj "something" ce biti stvoren i moze se koristiti
        # u modelu ali nema nikakvu poveznicu sa bazom podataka
        # jer nije definiran iznad kao db column - sqlalchemy
        # stvara konekciju izmedu pythona i baze podataka
        self.something = "hi"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

        return cls.query.filter_by(id=_id).first()
