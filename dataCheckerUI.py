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
        self.comparedResult = self.fileDataChecker.compareData()

        if(self.comparedResult == ""):
            T = Text(self.root,height=25,width=98)
            T.pack()
            T.place(x=5,y=90)
            T.insert(END,"The data in the two files are same")
            print("The data in the two files are same")
        else:
            T = Text(self.root,height=25,width=98)
            T.pack()
            T.place(x=5,y=90)
            T.insert(END,self.comparedResult)
            print(self.comparedResult)


dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
