import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Meal(Resource):
    # nesto za html forme, da se moze ici kroz forme preko ovog reqparsera...
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()      # decorator that makes - authentication required
    def get(self, name):
        try:
            meal = self.find_by_name(name)
        except:
            return {"message": "item not found.."}, 500
        if meal:
            return meal
        return {"message": "meal not found"}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM meals WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'meal': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': 'an meal with "{}" already exists.'.format(name)}, 400

        data = Meal.parser.parse_args()

        meal = {'name': name, 'price': data['price']}

        try:
            self.insert(meal)
        except:
            return {"message": "An error occured inserting item."}, 500

        return meal, 201

    @classmethod
    def insert(cls, meal):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO meals VALUES (?, ?)"
        cursor.execute(query, (meal['name'], meal['price']))

        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM meals WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        if self.find_by_name(name):
            pass
        return {'message': 'item deleted'}

    def put(self, name):
        data = Meal.parser.parse_args()

        meal = self.find_by_name(name)
        updated_meal = {'name': name,'price': data['price']}
        if meal is None:
            try:
                self.insert(updated_meal)
            except:
                return {"message": "Ann error occured inserting the meal."}, 500
        else:
            try:
                self.update(updated_meal)
            except:
                return {"message": "Ann error occured updating the meal."}, 500
        return meal

    @classmethod
    def update(cls, meal):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE meals SET price=? WHERE name=?"
        cursor.execute(query, (meal['price'], meal['name']))

        connection.commit()
        connection.close()


class MealList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM meals"
        result = cursor.execute(query)
        meals = []
        for row in result:
            meals.append({
                'name': row[0],
                'price': row[1]
            })

        connection.commit()
        connection.close()

        return {'meals': meals}
