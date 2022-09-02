from flask import Flask, request
from flask_restful import Api, Resource
from typing import Any, Dict
import argparse

app = Flask(__name__)
api = Api(app)
config: Dict[str, Any] = {}

class Top(Resource):
    def get(self):
        return "Pop'n Rhythmin Server!"

class RequestData():
    '''
    Deals with all request data, returns it how we want it.
    '''
    def get_request_data() -> Dict:
        data_dict = {}

        data = request.get_data()
        if data != None:
            data = data.decode('utf-8').split('&')
            for i in data:
                i_split = i.split('=')
                if len(i_split) == 2:
                    data_dict[f'{i_split[0]}'] = f'{i_split[1]}'

        return data_dict

    def put_request_data(data_dict) -> bytes:
        data = ''
        if data_dict == None:
            return None

        for key, val in data_dict.items():
            data = f'{data}{key}={val}&'

        return data.encode('utf-8')
        
class get_dl_file_list(Resource):
    def post(self):
        data = RequestData.get_request_data()
        print(data)

        return RequestData.put_request_data({'alloc': '', 'release': '200', 'date': '9/2/2022', 'retain': True})

# Service statics
uri_end = '/index.jsp'
uri_start = '/apr/main/cgi'

#add services
api.add_resource(Top, '/')
api.add_resource(get_dl_file_list, f'{uri_start}/get_dl_file_list{uri_end}')

def main() -> None:
    parser = argparse.ArgumentParser(description="3rd party server for Pop'n Rhythin.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()