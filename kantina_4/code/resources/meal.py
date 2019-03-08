from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.meal import MealModel


class Meal(Resource):
    TABLE_NAME = 'meals'

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Price cannot be left blank!"
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Description must exist! (1-200 characters)"
    )

    def get(self, name):
        meal = MealModel.find_by_name(name)
        if meal:
            return meal.json()
        return {'message': 'Item not found!'}, 404

    def post(self, name):
        if MealModel.find_by_name(name):
            return {'message': 'An item with name {} already exists.'.format(name)}

        data = Meal.parser.parse_args()
        meal = MealModel(name, data['price'], data['description'])

        try:
            meal.save_to_db()
        except:
            return {'message': 'Something went wrong with creating meal.'}, 500

        return meal.json()


    def delete(self, name):
        meal = MealModel.find_by_name(name)
        if meal:
            meal.delete_from_db()

        return {'message': 'Meal deleted'}

class MealList(Resource):
    TABLE_NAME = 'meals'

    def get(self):
        return {'meals': [meal.json() for meal in MealModel.query.all()]}

