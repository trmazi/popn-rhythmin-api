from flask import Flask
from flask_restful import Api, Resource
import argparse

from api.request import RequestData

app = Flask(__name__)
api = Api(app)

# Service statics
uri_start = '/apr/main/cgi'
uri_end = '/index.jsp'

@app.route('/')
def root():
    return "Pop'n Rhythmin Server!"

class get_event_info(Resource):
    def post(self):
        data = {'GamePlay': []}
        return data

class get_dl_file_list():
    def post(self):
        data = {'List': [
            {
                'Id': 0,
                'Url': 'https://iidxfan.xyz/dl0',
                'Size': 100
            },
            {
                'Id': 1,
                'Url': 'https://iidxfan.xyz/dl0',
                'Size': 100
            },
            {
                'Id': 2,
                'Url': 'https://iidxfan.xyz/dl0',
                'Size': 100
            }
        ]}
        return data

#add services
api.add_resource(get_dl_file_list, f'{uri_start}/get_dl_file_list{uri_end}')
api.add_resource(get_event_info, f'{uri_start}/get_event_info{uri_end}')

def main() -> None:
    parser = argparse.ArgumentParser(description="3rd party server for Pop'n Rhythin.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()