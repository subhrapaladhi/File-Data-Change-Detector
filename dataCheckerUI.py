from fileDataChecker import FileDataChecker
from tkinter import *
from tkinter import filedialog

class DataCheckerUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        
        title = Label(self.root, text = "File Data Checker") 
        title.config(font =("Courier", 35))
        title.place(x=150,y=20)

        # key text input
        self.keyLabel = Label(self.root, text="Enter key: ")
        self.keyLabel.config(font =("Courier", 15))
        self.keyLabel.place(x=220,y=120)
        self.passInput = Text(self.root,height=1,width=20)
        self.passInput.place(x=380,y=120)

        # choose button
        self.chooseBtn = Button(self.root, text="Choose File",command=self.chooseFile)
        self.chooseBtn.place(x=330,y=350)

        # check data
        self.checkDataBtn = Button(self.root, text="Check Data",command=self.dataCheck)
        self.checkDataBtn.pack()
        self.checkDataBtn.place(x=330,y=450)
        # self.printResult()

    
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
        T = Text(self.root,height=25,width=98)
        T.pack()
        T.place(x=5,y=90)
        dataUnchanged = self.fileDataChecker.compareData(T)

        if(dataUnchanged):
            #do something
            self.dataUnchangedLabel = Label(self.root, text="The Data in the two files is unchanged")
            self.dataUnchangedLabel.config(font =("Courier", 15))
            self.dataUnchangedLabel.place(x=170,y=550)
        else:
            self.dataUnchangedLabel = Label(self.root, text="The edited data is marked in red color")
            self.dataUnchangedLabel.config(font =("Courier", 15))
            self.dataUnchangedLabel.place(x=170,y=550)

# 45b5ca201e7b

dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
