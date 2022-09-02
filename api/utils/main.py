from flask import Flask
import json
import argparse

from api.request import RequestData

app = Flask(__name__)

# Service statics
uri_start = '/apr/main/cgi'
uri_end = '/index.jsp'

@app.route('/')
def root():
    return "Pop'n Rhythmin Server!"

@app.route(f'{uri_start}/get_event_info{uri_end}')
def get_event_info():
    return json.dumps({'GamePlay': []})

@app.route(f'{uri_start}/get_dl_file_list{uri_end}')
def get_dl_file_list():
    return json.dumps({'List': []})

def main() -> None:
    parser = argparse.ArgumentParser(description="3rd party server for Pop'n Rhythin.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()