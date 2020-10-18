from fileHasher import FileHasher
from tkinter import *
from tkinter import filedialog

class HasherUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x300")
        
        title = Label(self.root, text = "File Encrypter") 
        title.config(font =("Courier", 20))
        title.place(x=90,y=20)

    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        self.fileName = inputFile.name
        self.fileHasher = FileHasher(self.fileName)
        self.fileHasher.readFileData()
        self.saveData()

    def getFileName(self):
        self.chooseBtn = Button(self.root, text="Choose File",command=self.chooseFile)
        self.chooseBtn.place(x=150,y=200)
    


    def saveFun(self):
        self.fileHasher.saveData()
        l = Label(self.root, text="Save Successful", bg="red")
        l.place(x=100,y=150)

    def saveData(self):
        # get the key
        self.fileHasher.hasher()
        keyLabel = Label(self.root, text="Key = {} (Save it)".format(self.fileHasher.key), bg="red")
        keyLabel.place(x=95,y=120)

        # removing the choose file name
        self.chooseBtn.destroy()
        
        # saving data to database
        self.saveBtn = Button(self.root, text="Save",command=self.saveFun())
        self.saveBtn.place(x=150,y=200)
        self.saveBtn.destroy()

        
hasherUI = HasherUI()
hasherUI.getFileName()
# hasherUI.saveData()
hasherUI.root.mainloop()

# fileHasher = FileHasher("./data.txt") done
# fileHasher.readFileData() done
# fileHasher.hasher() 
# fileHasher.saveData()