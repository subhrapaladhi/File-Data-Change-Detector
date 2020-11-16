import hashlib
from pymongo import MongoClient
from tkinter import *
from tkinter import filedialog
import os

class FileDataChecker:
    def __init__(self,filename,key):
        self.filename = filename
        self.key = key

    def readFileData(self):
        file = open(self.filename,"rb")
        self.fileData = file.read()
        file.close()

    def getHasherData(self):
        client = MongoClient("mongodb+srv://subhra:<MONGODB KEY>@cluster0.stksg.mongodb.net/change_detector?retryWrites=true&w=majority")
        db = client['change_detector']
        hasher_data = db['hasher_data']
        x = hasher_data.find_one({"_id":self.key})

        if(x==None):
            return False
        
        self.salt = x["salt"]
        self.hashArray = x["hashedDataArray"]

        return True
    
    def hasher(self):
        self.editedFileHashArray = []
        self.editedFileUnhashedDataArray = []
        
        start = 0
        end = min(len(self.fileData),3)
        
        while(start<len(self.fileData)):
            if(end == len(self.fileData)+1):
                break
            substr = self.fileData[start:end]
            self.editedFileUnhashedDataArray.append(substr)
            result = hashlib.sha256(substr+self.salt).digest()
            self.editedFileHashArray.append(result)
            start +=1 
            end +=1
    
    def compareData(self,T):
        oriLen = len(self.hashArray)
        modLen = len(self.editedFileHashArray)
        
        dataUnchanged = True
        T.tag_configure("highlight",foreground="#FF0000")

        if(oriLen == modLen):
            for i in range(oriLen):
                if(self.editedFileHashArray[i] != self.hashArray[i]):
                    dataUnchanged = False
                    break
        else:       # modLen > orilen

            dataUnchanged = False

        return dataUnchanged

        