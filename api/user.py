from flask_restful import Resource
from api.request import RequestData

class get_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request == None:
            return {'ErrorCode': 'bad request!'}
        
        if request['uuid'] == None:
            return {'ErrorCode': 'bad uuid!'}

        return {}

class new_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            name = request['name']

            if uuid == None:
                return {'ErrorCode': 'bad uuid!'}
            if name == None:
                return {'ErrorCode': 'bad name!'}

        else: return {}, 200