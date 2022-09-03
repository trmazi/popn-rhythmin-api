from flask_restful import Resource
from api.request import RequestData

def bad_end(why) -> dict:
    print(f'Bad request data: {why}')
    return {'ErrorCode': why}

def format_player(uuid, name) -> dict:
    profile = {
        'PlayerId': uuid,
        'PlayerName': name,
        'InviteCnt': 1,
        'ArcadePt': 100,
        'FriendRequested': 1,
        'UpdateDate': '9/1/2022',
        'LoginBonusId': 0,
        'LoginCount': 69,
        'Login': 1,
    }
    print(profile)
    return profile

class get_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']

            if uuid == None:
                return bad_end('bad uuid!')

            return format_player(uuid, 'deez')

        else: return bad_end('bad request!')

class new_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            name = request['name']

            if uuid == None:
                return bad_end('bad uuid!')
            if name == None:
                return bad_end('bad name!')

            return format_player(uuid, name)

        else: return bad_end('bad request!')

class link_kid(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            konami_id = request['konami_id']
            password = request['password']

            if konami_id == None:
                return bad_end('bad konami_id!')
            if uuid == None:
                return bad_end('bad uuid!')
            if password == None:
                return bad_end('bad password!')

            return {
                'ErrorCode': 0
            }

        else: return bad_end('bad request!')