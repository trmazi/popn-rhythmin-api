from flask_restful import Resource
from api.request import RequestData

def bad_end(why) -> dict:
    print(f'Bad request data: {why}')
    return {'ErrorCode': why}

class get_recommend_list(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']

            if uuid == None:
                return bad_end('bad uuid!')

            return {
                'List': [],
                'Over': []
            }

        else: return bad_end('bad request!')