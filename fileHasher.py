import hashlib

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
        end = min(len(self.fileData),25)
        
        while(start<len(self.fileData)):
            substr = self.fileData[start:end]
            # print(substr)
            result = hashlib.sha256(substr).digest()
            self.hashArray.append(result)
            start = end
            end = min(len(self.fileData),end+25)
        
        # for i in self.hashArray:
        #     print(i)

fileHasher = FileHasher("./data.txt")
fileHasher.readFileData()
fileHasher.hasher()
