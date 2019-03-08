from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from meal import Meal, MealList


app = Flask(__name__)
app.secret_key = 'josip'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates endpoint "localhost/auth"

api.add_resource(Meal, '/meal/<string:name>')
api.add_resource(MealList, '/meals')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    # when we run app2.py, __main__ is file app2.py
    # ovaj if ce proci samo ako smo pokrenuli app2.py,
    # a nece se pokrenuti ako je main neki drugi file koji
    # importa ovaj file
    app.run(debug=True)

