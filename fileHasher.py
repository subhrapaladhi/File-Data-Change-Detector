class FileHasher:
    fileData = ""
    
    def __init__(self, filename):
        self.filename = filename

    def readFileData(self):
        file = open(self.filename,"rb")
        self.fileData = file.read()
        file.close()

fileHasher = FileHasher("./data.txt")
fileHasher.readFileData()
print(fileHasher.fileData)
