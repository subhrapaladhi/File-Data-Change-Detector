from fileHasher import FileHasher
from tkinter import *
from tkinter import filedialog

class HasherUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x300")
        
        title = Label(self.root, text = "File Encrypter") 
        title.config(font =("Courier", 20))
        title.place(x=100,y=20)

    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        self.fileName = inputFile.name
        print(self.fileName)
    
    def getFileName(self):
        btn = Button(self.root, text="Choose File",command=self.chooseFile)
        btn.place(x=150,y=150)
        self.root.mainloop()
        # btn = Button(root, text="Encrypt File",command=encryptFile)
        # btn.place(x=140,y=210)

        

hasherUI = HasherUI()
hasherUI.getFileName()


# fileHasher = FileHasher("./data.txt")
# fileHasher.readFileData()
# fileHasher.hasher()
# fileHasher.saveData()