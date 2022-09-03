import os
from flask_restful import Resource
from api.request import RequestData
from api.cdn.store.path import StorePath

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

class packlist(Resource):
    def get(self):
        filelist = []
        if os.path.exists(StorePath.getStorePath()):
            for subdir, dirs, files in os.walk(StorePath.getStorePath()):
                for filename in files:
                    if filename[-3:] != 'orb':
                        continue

                    filelist.append({
                        'ID': int(filename.replace('.orb', '')),
                    })

        print(f'Available store items: {filelist}')
        print(f'Promotions: {filelist}')
        return {
            'Version': '2.0.0',
            'PackList': filelist,
            'Promotion': filelist,
            'Error': 'The store is currently offline.\nPlease wait for it to be back!'
        }