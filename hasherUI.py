from fileHasher import FileHasher
from tkinter import *
from tkinter import filedialog

class HasherUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x300")
        
        title = Label(self.root, text = "File Hasher") 
        title.config(font =("Courier", 20))
        title.place(x=90,y=20)



    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        # self.fileName = inputFile.name
        self.fileHasher = FileHasher(inputFile.name)
        self.fileHasher.readFileData()
        self.saveData()

    def getFileName(self):
        self.chooseBtn = Button(self.root, text="Choose File",command=self.chooseFile)
        self.chooseBtn.place(x=150,y=200)
    


    def saveFun(self):
        self.fileHasher.saveData()
        saveLabel = Label(self.root, text="Save Successful", bg="yellow")
        saveLabel.place(x=140,y=150)

    def saveData(self):
        # get the key
        self.fileHasher.hasher()
        T = Text(self.root,height=1,width=28,padx=0.5)
        T.pack()
        T.place(x=95,y=90)
        T.insert(END,"Key = {} (Save it)".format(self.fileHasher.key))

        # removing the choose file name
        self.chooseBtn.destroy()
        
        # saving data to database
        self.saveBtn = Button(self.root, text="Save",command=self.saveFun)
        self.saveBtn.place(x=160,y=230)
        

        
hasherUI = HasherUI()
hasherUI.getFileName()
hasherUI.root.mainloop()