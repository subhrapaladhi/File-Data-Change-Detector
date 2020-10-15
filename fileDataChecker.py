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
        self.unhashedDataArray = x["unhashedDataArray"]
        self.hashArray = x["hashedDataArray"]
    
    def hasher(self):
        self.editedFileHashArray = []
        self.editedFileUnhashedDataArray = []
        
        start = 0
        end = min(len(self.fileData),5)
        
        while(start<len(self.fileData)):
            if(end == len(self.fileData)+1):
                break
            substr = self.fileData[start:end]
            self.editedFileUnhashedDataArray.append(substr)

            result = hashlib.sha256(substr).digest()
            self.editedFileHashArray.append(result)
            start +=1 
            end +=1
            print(substr)
            print(result)

fileDataChecker = FileDataChecker("./data.txt","803471303176")
fileDataChecker.readFileData()
fileDataChecker.getHasherData()
fileDataChecker.hasher()