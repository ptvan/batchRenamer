from tkinter import INSERT, Tk, Frame, Button, Entry, Checkbutton, Text, IntVar, filedialog, messagebox
import sys

class batchRenamer(Frame):

    def __init__(self, master=None):
        # window = tk.Tk()
        # window.title("File Renamer")
        Frame.__init__(self, master)
        self.master.rowconfigure(1, weight=3)
        self.grid()

        self.browseBtn = Button(self, text="select files", command=self.browseFiles)
        self.browseBtn.grid(row=0, column=0)

        self.oldNames = Text(self, width=50, height=5)
        self.oldNames.grid(row=1, column=0, columnspan=3)
        
        self.prefixOn = IntVar()
        self.prefixChkbox = Checkbutton(self, text="prefix", variable=self.prefixOn) 
        self.prefixChkbox.grid(row=2, column=0)
        self.prefixEdit = Entry(self, width=10)
        self.prefixEdit.grid(row=2, column=1)

        self.suffixOn = IntVar()
        self.suffixChkbox = Checkbutton(self, text="suffix", variable=self.suffixOn)
        self.suffixChkbox.grid(row=3, column=0) 
        self.suffixEdit = Entry(self, width=10)
        self.suffixEdit.grid(row=3, column=1)

        self.numberingOn = IntVar()
        self.numberingChkbox = Checkbutton(self, text="numbering", variable=self.numberingOn)
        self.numberingChkbox.grid(row=4, column=0) 
        self.numberingStartEdit = Entry(self, width=5)
        self.numberingStartEdit.grid(row=4, column=1)
        self.numberingStepEdit = Entry(self, width=5)
        self.numberingStepEdit.grid(row=4, column=2)

        self.replaceOn = IntVar()
        self.replaceChkbox = Checkbutton(self, text="replace", variable=self.replaceOn)
        self.replaceChkbox.grid(row=5, column=0) 
        self.replaceOldEdit = Entry(self)
        self.replaceOldEdit.grid(row=5, column=1)
        self.replaceNewEdit = Entry(self)
        self.replaceNewEdit.grid(row=5, column=2)

        self.newNames = Text(self, width=50, height=5)
        self.newNames.grid(row=6, column=0, columnspan=3)
        
        self.renameBtn = Button(self, text="rename", command=self.confirm)
        self.renameBtn.grid(row=7, column=0)

        
    def browseFiles(self):
        files = filedialog.askopenfilenames(title="Select files to rename")
        print(files)
        self.oldNames.insert(INSERT, files)

    def processNames(self):
        if self.prefixOn == True:
            print("prefix")

        if self.suffixOn == True:
            print("suffix")
        
        if self.numberingOn == True:
            print("numbering")
        
        if self.replaceOn == True:
            print("replace")

    def confirm(self):
        messagebox.askyesno('Confirm file rename', 'Rename files ?')
    
    def renameFiles(self):
        print("renaming files!")


root = Tk()
root.title('Batch Renamer')
root.geometry("620x500")

app = batchRenamer(root)

root.mainloop()
root.destroy()
