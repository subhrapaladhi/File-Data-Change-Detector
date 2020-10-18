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
    
    def compareData(self):
        oriLen = len(self.hashArray)
        modLen = len(self.editedFileHashArray)
        print("orilen = {} || modlen = {}".format(oriLen,modLen))
        if(oriLen == modLen):
            i = 0
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    origData = self.unhashedDataArray[i]
                    editedData = self.editedFileUnhashedDataArray[i]
                    print("Original Data: {} VS Edited Data: {}".format(origData,editedData))
                i+=1

        elif(oriLen > modLen):
            i = 0
            while(i<modLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    origData = self.unhashedDataArray[i]
                    editedData = self.editedFileUnhashedDataArray[i]
                    print("Original Data: {} VS Edited Data: {}".format(origData,editedData))
                i+=1

            i = modLen
            leftData = ""
            while(i<oriLen):
                temp = str(self.unhashedDataArray[i],"utf-8")
                leftData += temp[-1]
                i+=1

            print("This data is not there in the edited data: {}".format(leftData))
    

        else:       # modLen > orilen
            i = 0
            while(i<oriLen):
                if(self.hashArray[i] != self.editedFileHashArray[i]):
                    origData = self.unhashedDataArray[i]
                    editedData = self.editedFileUnhashedDataArray[i]
                    print("Original Data: {} VS Edited Data: {}".format(origData,editedData))
                i+=1

            i = oriLen
            leftData = ""
            while(i<modLen):
                temp = str(self.editedFileUnhashedDataArray[i],"utf-8")
                leftData += temp[-1]
                i+=1

            print("This data is not there in the original data: {}".format(leftData))