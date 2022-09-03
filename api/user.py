from flask_restful import Resource
from api.request import RequestData

def bad_end(why) -> dict:
    print(f'Bad request data: {why}')
    return {'ErrorCode': why}

def format_player(uuid, name) -> dict:
    profile = {
        'PlayerId': '1234567',
        'PlayerName': name,
        'InviteCnt': 1,
        'ArcadePt': 100,
        'FriendRequested': 0,
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
                return bad_end(1)

            return format_player(uuid, 'deez')

        else: return bad_end(1)

class new_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            name = request['name']

            if uuid == None:
                return bad_end(1)
            if name == None:
                return bad_end(1)

            return format_player(uuid, name)

        else: return bad_end(1)

class link_kid(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            konami_id = request['konami_id']
            password = request['password']

            if konami_id == None:
                return bad_end(1)
            if uuid == None:
                return bad_end(1)
            if password == None:
                return bad_end(1)

            return {
                'ErrorCode': 2,
            }

        else: return bad_end(1)

class invited(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']
            player_id = request['player_id']

            if uuid == None:
                return bad_end(4)
            if player_id == None:
                return bad_end(4)

            return {
                'ErrorCode': 2,
            }

        else: return bad_end(4)