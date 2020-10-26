from fileHasher import FileHasher
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk

class HasherUI:
    def __init__(self):
        # self.root = Tk()
        self.root = tk.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("plastik")
        self.root.geometry("800x600")
        self.root.configure(bg="#F0BF5A")
        
        title = Label(self.root, text = "File Hasher",font="Times 40 bold",bg="#F0BF5A") 
        title.place(x=260,y=40)



    def chooseFile(self):
        inputFile = filedialog.askopenfile(mode="r")
        # self.fileName = inputFile.name
        self.fileHasher = FileHasher(inputFile.name)
        self.fileHasher.readFileData()
        self.saveData()

    def getFileName(self):
        self.chooseBtn = Button(self.root, 
                                text="Choose File",
                                command=self.chooseFile,
                                bg="#2F97BA",
                                fg="#000000",
                                activeforeground="#4B574F",
                                activebackground="#6DD88E",
                                font="arial 15",
                                pady=2,
                                )
        self.chooseBtn.place(x=320,y=460)
    


    def saveFun(self):
        self.fileHasher.saveData()
        saveLabel = Label(self.root, 
                        text="Save Successful", 
                        bg="#F0BF5A",
                        fg="#000000",
                        font="arial 22 bold",
                        pady=10,
                        padx=5)
        saveLabel.place(x=280,y=430)

    def saveData(self):
        # get the key
        self.fileHasher.hasher()
        T = Text(self.root,height=1,width=28,padx=5,pady=5,font="Times 20 bold",bg="#B5F1AE")
        T.pack()
        T.place(x=200,y=200)
        T.insert(END,"Your File Key = {}".format(self.fileHasher.key))

        # removing the choose file name
        self.chooseBtn.destroy()
        
        # saving data to database
        self.saveBtn = Button(  self.root, 
                                text="Save",
                                command=self.saveFun,
                                bg="#2F97BA",
                                fg="#000000",
                                activeforeground="#4B574F",
                                activebackground="#6DD88E",
                                font="arial 20",
                                pady=5)

        self.saveBtn.place(x=360,y=430)
        

        
hasherUI = HasherUI()
hasherUI.getFileName()
hasherUI.root.mainloop()