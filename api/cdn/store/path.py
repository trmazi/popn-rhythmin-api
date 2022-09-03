import os

class StorePath:
    def getStorePath():
        return os.path.abspath(os.path.dirname(__file__))