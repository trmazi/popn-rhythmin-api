from flask_restful import Resource
from api.request import RequestData

class get_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request == None:
            return {'ErrorCode': 'bad request!'}
        
        if request['uuid'] == None:
            return {'ErrorCode': 'bad uuid!'}

        print(request['uuid'])