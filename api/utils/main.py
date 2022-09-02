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
        
class get_dl_file_list(Resource):
    def post(self):
        print(request.get_json())
        return {'balls'}

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