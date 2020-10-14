import hashlib
from pymongo import MongoClient
import uuid


class FileHasher:
    fileData = ""
    
    def __init__(self, filename):
        self.filename = filename

    def readFileData(self):
        file = open(self.filename,"rb")
        self.fileData = file.read()
        file.close()

    def hasher(self):
        self.hashArray = []
        self.unhashedDataArray = []
        
        start = 0
        end = min(len(self.fileData),5)
        
        while(start<len(self.fileData)):
            if(end == len(self.fileData)+1):
                break
            substr = self.fileData[start:end]
            self.unhashedDataArray.append(substr)

            result = hashlib.sha256(substr).digest()
            self.hashArray.append(result)
            start +=1 
            end +=1

    def saveData(self):
        client = MongoClient("mongodb+srv://subhra:qWT6ZfofeDcQoXnn@cluster0.stksg.mongodb.net/change_detector?retryWrites=true&w=majority")
        db = client['change_detector']
        collection = db['hashed_data']

        self.key = str(uuid.uuid4())[-12:]
        print("key = {}".format(self.key))
        data = {"_id": self.key, "hashedData": self.hashArray, "unhashedData": self.unhashedDataArray}

        # print(client.list_database_names())
        # print(db.list_collection_names())
        # x = collection.insert_one({"_id":"12345","name":"subhra"})
        # print(x)

fileHasher = FileHasher("./data.txt")
fileHasher.readFileData()
fileHasher.hasher()
fileHasher.saveData()