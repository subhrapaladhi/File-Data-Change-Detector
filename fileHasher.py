import hashlib
from pymongo import MongoClient

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
        
        start = 0
        end = min(len(self.fileData),5)
        
        while(start<len(self.fileData)):
            if(end == len(self.fileData)+1):
                break
            substr = self.fileData[start:end]
            print(substr)
            result = hashlib.sha256(substr).digest()
            print(result)
            self.hashArray.append(result)
            start +=1 
            end +=1
    def saveData(self):
        client = MongoClient("mongodb+srv://subhra:qWT6ZfofeDcQoXnn@cluster0.stksg.mongodb.net/change_detector?retryWrites=true&w=majority")
        db = client['change_detector']
        collection = db['hashed_data']

        print(client.list_database_names())
        print(db.list_collection_names())
        x = collection.insert_one({"_id":"12345","name":"subhra"})
        print(x)

fileHasher = FileHasher("./data.txt")
fileHasher.readFileData()
fileHasher.hasher()
fileHasher.saveData()
