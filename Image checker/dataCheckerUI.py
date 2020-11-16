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
        self.root.geometry("700x500")
        self.root.configure(bg="#F0BF5A")
        
        title = Label(self.root, text = "Image Checker",font="Times 30 bold",bg="#F0BF5A") 
        title.place(x=220,y=40)

        # key text input
        self.keyLabel = Label(self.root, text="Enter key: ", font="Times 20 bold",bg="#F0BF5A")
        self.keyLabel.place(x=180,y=150)
        self.passInput = Text(self.root,height=1.25,width=20,font="Times 15",bg="#F8EBDB",padx=5,pady=3)
        self.passInput.place(x=320,y=150)

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
        self.chooseBtn.place(x=270,y=320)

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
        self.checkDataBtn.place(x=270,y=420)
        
    
    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        self.fileName = inputFile.name
        fileName = inputFile.name
        file = fileName.split('/')[-1]
        fileNameLabel = Label(self.root, 
                        text="Selected File: ", 
                        bg="#F0BF5A",
                        fg="#000000",
                        font="arial 12 bold",
                        pady=10,
                        padx=5)
        fileNameLabel.place(x=230,y=225)

        fileNameDisplay = Label(self.root, 
                        text=file, 
                        bg="#F0BF5A",
                        fg="#000000",
                        font="arial 12",
                        pady=10,
                        padx=5)
        fileNameDisplay.place(x=350,y=225)


    def dataCheck(self):
        self.key = str(self.passInput.get(1.0,END)).strip()
        print("key = {}".format(self.key))

        self.fileDataChecker = FileDataChecker(self.fileName,self.key)
        self.fileDataChecker.readFileData()
        keyValid = self.fileDataChecker.getHasherData()

        if(keyValid):
            self.fileDataChecker.hasher()
            print("valid key")
            T = Text(self.root,height=15,width=58,padx=10,pady=10,font="Times 14",bg="#EAF6F3")
            T.pack()
            T.place(x=75,y=120)
            self.checkDataBtn.place(x=325,y=250)

            dataUnchanged = self.fileDataChecker.compareData(T)

            if(dataUnchanged):
                self.dataUnchangedLabel = Label(self.root, text="The new image matches the old image",font="Times 20 bold",bg="#42aaf5")
                self.dataUnchangedLabel.place(x=120,y=250)
            else:
                self.dataUnchangedLabel = Label(self.root, text="The new image does not match the old image",font="Times 20 bold",bg="#f59342")
                self.dataUnchangedLabel.place(x=100,y=250)
        
        else:
            print("invalid key")
            self.invalidKeyLabel = Label(self.root, text="Key Not Valid", font="Times 30 bold",bg="#F0BF5A")
            self.invalidKeyLabel.place(x=500,y=400)

dataCheckerUI = DataCheckerUI()
dataCheckerUI.root.mainloop()
