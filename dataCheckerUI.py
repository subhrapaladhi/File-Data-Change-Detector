from fileDataChecker import FileDataChecker
from tkinter import *
from tkinter import filedialog

class DataCheckerUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x300")
        
        title = Label(self.root, text = "File Data Checker") 
        title.config(font =("Courier", 20))
        title.place(x=90,y=20)

        # key text input
        self.keyLabel = Label(self.root, text="Enter key: ")
        self.keyLabel.place(x=65,y=80)
        self.passInput = Text(self.root,height=1,width=20)
        self.passInput.place(x=100,y=80)

        # choose button
        self.chooseBtn = Button(self.root, text="Choose File",command=self.chooseFile)
        self.chooseBtn.place(x=150,y=180)

        # check data
        self.checkDataBtn = Button(self.root, text="Check Data",command=self.dataCheck)
        self.checkDataBtn.place(x=150,y=220)
    
    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        self.fileName = inputFile.name
        print(self.fileName)
    
    def dataCheck(self):
        self.key = str(self.passInput.get(1.0,END)).strip()
        print("key = {}".format(self.key))

        self.fileDataChecker = FileDataChecker(self.fileName,self.key)
        self.fileDataChecker.readFileData()
        self.fileDataChecker.getHasherData()
        self.fileDataChecker.hasher()
        comparedResult = self.fileDataChecker.compareData()

        if(comparedResult == ""):
            print("The data in the two files are same")
        else:
            print(comparedResult)


dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
