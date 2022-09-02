from flask_restful import Resource
from api.request import RequestData

class get_event_info(Resource):
    def post(self):
        return {'GamePlay': []}

class get_dl_file_list(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request['client_ver'] != '200':
            return {'ErrorCode': 'wrong client!'}
            
        return {'List': []}