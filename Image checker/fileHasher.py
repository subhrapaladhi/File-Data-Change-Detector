import hashlib
from pymongo import MongoClient
import uuid
import os


class FileHasher:    
    def __init__(self, filename):
        self.filename = filename

    def readFileData(self):
        file = open(self.filename,"rb")
        self.fileData = file.read()
        # print('filedata = \n',self.fileData)
        file.close()

    def hasher(self):
        self.hashArray = []
        self.unhashedDataArray = []
        
        start = 0
        end = min(len(self.fileData),3)
        self.salt = os.urandom(6)
        while(start<len(self.fileData)):
            if(end == len(self.fileData)+1):
                break
            substr = self.fileData[start:end]
            self.unhashedDataArray.append(substr)
            result = hashlib.sha256(substr+self.salt).digest()
            self.hashArray.append(result)
            start +=1 
            end +=1
        
        self.key = str(uuid.uuid4())[-12:]
        print("key = {}".format(self.key))

    def saveData(self):
        client = MongoClient("mongodb+srv://subhra:<MONGODB KEY>@cluster0.stksg.mongodb.net/change_detector?retryWrites=true&w=majority")
        db = client['change_detector']
        hasher_data = db['hasher_data']
        data = {"_id": self.key, "salt":self.salt, "hashedDataArray": self.hashArray, "unhashedDataArray": self.unhashedDataArray}
        hasher_data.insert_one(data)