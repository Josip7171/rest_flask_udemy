from flask_restful import Resource, reqparse
from models.user_info import UserInfoModel
from models.user import UserModel
import datetime


class UserFill(Resource):
    TABLE_NAME = 'user_info'

    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str
                        )
    parser.add_argument('last_name',
                        type=str
                        )
    parser.add_argument('full_name',
                        type=str
                        )
    parser.add_argument('adress',
                        type=str
                        )
    parser.add_argument('postal_code',
                        type=int
                        )
    parser.add_argument('phone_number',
                        type=str
                        )
    parser.add_argument('birth_date',
                        type=str
                        )
    parser.add_argument('gender',
                        type=str
                        )

    # ovo treba biti PUT! a postaviti sve na defaultne vrijednosti...
    def post(self, user_id):
        dt = datetime.datetime.utcnow()
        print(UserModel.find_by_id(user_id))
        if UserModel.find_by_id(user_id) is None:
            return {'message': "User with id {} does NOT exist.".format(user_id)}

        data = UserFill.parser.parse_args()
        # user_info = UserInfoModel(user_id, data['first_name'], data['last_name'], data['full_name'],
        #                           data['adress'], data['postal_code'], data['phone_number'],
        #                           data['birth_date'], data['gender'], data['avatar'])

        user_info = UserInfoModel(user_id, **data)
        user_info.save_to_db()

        return {"message": "User info updated successfully."}, 201