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
        print(self.fileName)
        self.fileHasher = FileHasher(self.fileName)
        self.fileHasher.readFileData()
        # print(self.fileHasher.fileData)
        self.fileHasher.hasher()
        l = Label(self.root, text="Key = {} (Save it)".format(self.fileHasher.key), bg="red")
        l.place(x=95,y=120)


    def getFileName(self):
        btn = Button(self.root, text="Choose File",command=self.chooseFile)
        btn.place(x=150,y=200)
        
        self.root.mainloop()  
        
hasherUI = HasherUI()
hasherUI.getFileName()


# fileHasher = FileHasher("./data.txt") done
# fileHasher.readFileData() done
# fileHasher.hasher() 
# fileHasher.saveData()