from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    TABLE_NAME = 'store'

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

    # @jwt_required()
    # def put(self, name):
    #     data = Item.parser.parse_args()
    #     item = ItemModel.find_by_name()
    #
    #     if item is None:
    #         item = ItemModel(name, data['price'], data['store_id'])
    #         # or :
    #         # item = ItemModel(name, **data)
    #     else:
    #         item.price = data['price']
    #
    #     item.save_to_db()
    #     return item.json()

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # ili :
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
