import hashlib
from pymongo import MongoClient
from tkinter import *
from tkinter import filedialog

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
        end = min(len(self.fileData),3)
        
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
            # print(result)
    
    def compareData(self,T):
        oriLen = len(self.hashArray)
        modLen = len(self.editedFileHashArray)
        print("orilen = {} || modlen = {}".format(oriLen,modLen))
        comparedResult = ""
        if(oriLen == modLen):

            # if(self.hashArray[0] == self.editedFileHashArray[0]):
            T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            i = 1
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    # highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                else:
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])

                i+=1

        elif(oriLen > modLen):
            # if(self.hashArray[0] == self.editedFileHashArray[0]):
            T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            i = 1
            while(i<modLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                else:
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                i+=1

            i = modLen
            while(i<oriLen):
                #highlight this text
                temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                T.insert(END,temp[-1])
                i+=1

        else:       # modLen > orilen
            # if(self.hashArray[0] == self.editedFileHashArray[0]):
            T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            i = 1
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                else:
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                i+=1

            i = oriLen    
            while(i<modLen):
                temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                T.insert(END,temp[-1])
                i+=1



# fileDataChecker = FileDataChecker("./data.txt","a5e099824b50")
# fileDataChecker.readFileData()
# fileDataChecker.getHasherData()
# fileDataChecker.hasher()
# fileDataChecker.compareData()