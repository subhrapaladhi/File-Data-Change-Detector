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
        self.root.geometry("1200x900")
        self.root.configure(bg="#F0BF5A")
        
        title = Label(self.root, text = "File Data Checker",font="Times 40 bold",bg="#F0BF5A") 
        title.place(x=390,y=40)

        # key text input
        self.keyLabel = Label(self.root, text="Enter key: ", font="Times 20 bold",bg="#F0BF5A")
        self.keyLabel.place(x=420,y=200)
        self.passInput = Text(self.root,height=1.25,width=20,font="Times 15",bg="#F8EBDB",padx=5,pady=3)
        self.passInput.place(x=600,y=200)

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
        self.chooseBtn.place(x=540,y=550)

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
        self.checkDataBtn.place(x=540,y=725)
        
    
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

        T = Text(self.root,height=35,width=115,padx=10,pady=10,font="Times 14",bg="#EAF6F3")
        T.pack()
        T.place(x=75,y=120)
        message = self.fileDataChecker.compareData(T)
        self.checkDataBtn.place(x=325,y=450)
        self.dataUnchangedLabel = Label(self.root, text=message,font="Times 20 bold",bg="#F0BF5A")
        self.dataUnchangedLabel.place(x=390,y=840)

dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
