import os

class StockPath:
    def getStockPath():
        return os.path.abspath(os.path.dirname(__file__))