from flask import Flask
from flask_restful import Api, Resource
from typing import Any, Dict
import argparse

app = Flask(__name__)
api = Api(app)
config: Dict[str, Any] = {}

class Top(Resource):
    def get(self):
        return "Pop'n Rhythmin Server!"

#add services
api.add_resource(Top, '/')

def main() -> None:
    parser = argparse.ArgumentParser(description="3rd party server for Pop'n Rhythin.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 8020", type=int, default=8020)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()