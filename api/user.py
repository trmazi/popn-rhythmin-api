from flask_restful import Resource
from api.request import RequestData

def format_player(uuid) -> dict:
    profile = {
        'PlayerID': '1',
        'PlayerName': 'FUCK',
        'InviteCnt': 100,
        'ArcadePt': 1000,
        'FriendRequested': 0,
        'UpdateDate': '9/1/2022',
        'LoginBonusId': 1,
        'LoginCount': 69,
        'Login': True,
    }
    return profile

class get_player(Resource):
    def post(self):
        request = RequestData.get_request_data()
        if request != None:
            uuid = request['uuid']

            if uuid == None:
                return {'ErrorCode': 'bad uuid!'}

            return format_player(uuid)

        else: return {'ErrorCode': 'Bad request!'}, 200

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

            return format_player(uuid)

        else: return {'ErrorCode': 'Bad request!'}, 200