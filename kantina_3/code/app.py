from flask import Flask, render_template, jsonify, request


app = Flask(__name__)
users = [
    {
        'name': 'JosipR',
        'meal': [
            {
                'name': 'Grah',
                'price': 25.00
            }
        ]
    }
]


@app.route('/user', methods=["POST"])
def create_user():
    request_data = request.get_json()
    print(request_data)
    new_user = {
        'name': request_data['name'],
        'meal' : []
    }
    users.append(new_user)
    return jsonify(new_user)


@app.route('/user/<string:name>')
def get_user(name):
    for user in users:
        if name == user['name']:
            return jsonify(user)
    return jsonify({'message': 'user not found!'})


@app.route('/user')
def get_users():
    return jsonify({'users': users})


@app.route('/user/<string:name>/meal', methods=["POST"])
def create_meal_of_user(name):
    request_data = request.get_json()
    print(request_data)
    for user in users:
        if name == user['name']:
            new_meal = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            user['meal'].append(new_meal)
            return jsonify(new_meal)
    return jsonify({'message': 'user not found!'})


@app.route('/user/<string:name>/meal')
def get_meal_of_user(name):
    for user in users:
        if name == user['name']:
            return jsonify({'meal': user['meal']})
    return jsonify({'message', 'user not found!'})


@app.route('/')
def home():
    return render_template("index.html")


app.run(debug=True)
