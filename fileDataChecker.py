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
        comparedResult = ""
        extraText=""
        dataUnchanged = True
        T.tag_configure("highlight",foreground="#FF0000")

        if(oriLen == modLen):

            if(self.hashArray[0] == self.editedFileHashArray[0]):
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            else:
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")),"highlight")
            i = 1
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    # highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1],"highlight")
                    dataUnchanged = False
                else:
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])

                i+=1

        elif(oriLen > modLen):
            if(self.hashArray[0] == self.editedFileHashArray[0]):
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            else:
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")),"highlight")
            i = 1
            dataUnchanged = False
            while(i<modLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1],"highlight")
                else:
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                i+=1

        else:       # modLen > orilen
            if(self.hashArray[0] == self.editedFileHashArray[0]):
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")))
            else:
                T.insert(END,"{}".format(str(self.editedFileUnhashedDataArray[0],"utf-8")),"highlight")
            i = 1
            dataUnchanged = False
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1],"highlight")
                else:
                    #highlight this text
                    temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                    T.insert(END,temp[-1])
                i+=1

            i = oriLen    
            while(i<modLen):
                temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                T.insert(END,temp[-1],"highlight")
                i+=1
        message=""

        if(dataUnchanged):
            message = "The Data in the two files is unchanged"
        else:
            if(oriLen==modLen):
                message="The edited data is marked in red color"
            elif(oriLen<modLen):
                message="Some data is extra in the Edited file"
            else:
                message="Some data is missing from the Edited file"

        return message

        