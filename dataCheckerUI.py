from fileDataChecker import FileDataChecker
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk

class DataCheckerUI:
    def __init__(self):
        # self.root = Tk()
        self.root = tk.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("plastik")
        self.root.geometry("800x600")
        self.root.configure(bg="#F0BF5A")
        
        title = Label(self.root, text = "File Data Checker",font="Times 40 bold",bg="#F0BF5A") 
        title.place(x=170,y=20)

        # key text input
        self.keyLabel = Label(self.root, text="Enter key: ", font="Times 20 bold",bg="#F0BF5A")
        self.keyLabel.place(x=220,y=120)
        self.passInput = Text(self.root,height=1.25,width=20,font="Times 15",bg="#F8EBDB")
        self.passInput.place(x=380,y=120)

        # choose button
        self.chooseBtn = Button(self.root, 
                                text="Choose File",
                                command=self.chooseFile,
                                bg="#2F97BA",
                                fg="#000000",
                                activeforeground="#4B574F",
                                activebackground="#6DD88E",
                                font="Times 17 bold"
                                )
        self.chooseBtn.place(x=325,y=380)

        # check data
        self.checkDataBtn = Button(self.root, 
                                    text="Check Data",
                                    command=self.dataCheck,
                                    bg="#2F97BA",
                                    fg="#000000",
                                    activeforeground="#4B574F",
                                    activebackground="#6DD88E",
                                    font="Times 17 bold"
                                    )
        
        self.checkDataBtn.pack()
        self.checkDataBtn.place(x=325,y=500)
        
    
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
            self.dataUnchangedLabel = Label(self.root, text="The Data in the two files is unchanged",font="Times 20 bold",bg="#F0BF5A")
            self.dataUnchangedLabel.place(x=170,y=550)
        else:
            self.dataUnchangedLabel = Label(self.root, text="The edited data is marked in red color",font="Times 20 bold",bg="#F0BF5A")
            self.dataUnchangedLabel.place(x=170,y=550)

# 45b5ca201e7b

dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
