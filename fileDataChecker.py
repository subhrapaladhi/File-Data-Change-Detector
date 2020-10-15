import hashlib
from pymongo import MongoClient

class FileDataChecker:
    def __init__(self,filename,key):
        self.filename = filename
        self.key = key
    
    def readFileData(self):
        file = open(self.filename,"rb")
        self.fileData = file.read()
        file.close()

    def getHasherData(self):
        client = MongoClient("mongodb+srv://subhra:qWT6ZfofeDcQoXnn@cluster0.stksg.mongodb.net/change_detector?retryWrites=true&w=majority")
        db = client['change_detector']
        hasher_data = db['hasher_data']

        x = hasher_data.find_one({"_id":self.key})
        print(x)

fileDataChecker = FileDataChecker("./data.txt","803471303176")
fileDataChecker.getHasherData()