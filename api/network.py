from flask_restful import Resource

class search_master(Resource):
    def get(self):
        response = {
            'GameCenterList': [
                {
                    'ID': 0,
                    'Lat': 39.908987,
                    'Long': -86.065242,
                    'Name': 'Boss Battle Games',
                    'Open': '1',
                    'Model': [1]
                }
            ],
            'Version': '2.0.0',
            'Info': 'Da Map.',
            'Mark': [
                {
                   'Order': '1',
                   'Model': '0',
                   'Name': 'Boss Battle Games',
                   'Image': 'https://shorturl.at/emruW'
                }
            ]
        }

        print(response)
        return response