from flask_restful import Resource
from api.request import RequestData

class get_player(Resource):
    def post(self):
        print(RequestData.get_request_data())