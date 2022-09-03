import os
from flask_restful import Resource
from api.request import RequestData
from api.cdn.stock.path import StockPath

class get_event_info(Resource):
    def post(self):
        return {'GamePlay': []}

class get_dl_file_list(Resource):
    '''
    This is used to download the stock music, so that the game has something to download.
    We shall put these in /api/cdn/stock
    Store music will be in /api/cdn/store
    '''
    def post(self):
        request = RequestData.get_request_data()
        if request['client_ver'] != '200':
            return {'ErrorCode': '4'}

        filelist = []
        index = 0

        if os.path.exists(StockPath.getStockPath()):
            for subdir, dirs, files in os.walk(StockPath.getStockPath()):
                for filename in files:
                    if filename == 'path.py':
                        continue

                    print({StockPath.getStockPath()}/{filename})
                    filelist.append({
                        'Id': index,
                        'Url': f'https://popapp.ez4dj.com/cdn/stock/{filename}',
                        'Size': os.path.getsize(f'{StockPath.getStockPath()}/{filename}')
                    })
            
        return {'List': filelist}