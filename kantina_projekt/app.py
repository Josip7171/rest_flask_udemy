from flask import Flask, render_template, json, url_for, redirect, flash
from flask_restful import Api
from flask_jwt import JWT
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from forms.user_form import RegistrationForm
from models.user_user import User, UserDetails


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home_page.html", title="HOME PAGE", heading1="HOME PAGE")


@app.route("/about")
def about_page():
    return render_template("about_page.html", title="ABOUT PAGE", heading1="ABOUT PAGE")


@app.route("/test_api", methods=["GET", "POST"])
def test_api():
    data = {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key3_1": "value3_1",
            "key3_2": "value3_2"
        },
        "key4": "value4",
        "key5": {
            "key5_1":{
                "key5_1_1": "value5_1_1",
                "key5_1_2": "value%_1_2"
            },
            "key5_2": {
                "key5_2_1": "value5_2_1",
                "key5_2_2": "value%_2_2"
            }
        }
    }

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/registerr", methods=["POST", "GET"])
def registerr():
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(full_name=form.full_name.data, email=form.email.data,
                    password=hashed_password, first_name=form.first_name.data,
                    last_name=form.last_name.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Youre now able to login.', 'success')
        return redirect(url_for("home_page"))
    return render_template("register.html", title='Register', form=form)




if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

