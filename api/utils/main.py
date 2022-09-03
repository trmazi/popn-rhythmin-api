from flask import Flask
from flask_restful import Api
import argparse

from api.events import get_dl_file_list, get_event_info
from api.user import get_player, new_player
from api.network import search_master

app = Flask(__name__)
api = Api(app)

# Service statics
uri_start = '/apr/main/cgi'
uri_end = '/index.jsp'

@app.route('/')
def root():
    return "Pop'n Rhythmin Server!"

@app.route('/apr/main/cgi/new/index.jsp')
def new():
    return "Welcome!"

#add services
api.add_resource(get_dl_file_list, f'{uri_start}/get_dl_file_list{uri_end}')
api.add_resource(get_event_info, f'{uri_start}/get_event_info{uri_end}')
api.add_resource(get_player, f'{uri_start}/get_player{uri_end}')
api.add_resource(new_player, f'{uri_start}/new_player{uri_end}')
api.add_resource(search_master, f'{uri_start}/search_master{uri_end}')

def main() -> None:
    parser = argparse.ArgumentParser(description="3rd party server for Pop'n Rhythin.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()