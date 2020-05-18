from tkinter import INSERT, Tk, Frame, Button, Entry, Checkbutton, Text, IntVar, filedialog, messagebox
import sys
import os

class batchRenamer(Frame):

    def __init__(self, master=None):
        # window = tk.Tk()
        # window.title("File Renamer")
        Frame.__init__(self, master)
        self.master.rowconfigure(1, weight=3)
        self.grid()

        self.browseBtn = Button(self, text="select files", command=self.browseFiles)
        self.browseBtn.grid(row=0, column=0)

        self.oldEdit = Text(self, width=50, height=5)
        self.oldEdit.grid(row=1, column=0, columnspan=3)
        
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

        self.newEdit = Text(self, width=50, height=5)
        self.newEdit.grid(row=6, column=0, columnspan=3)
        
        self.renameBtn = Button(self, text="rename", command=self.confirm)
        self.renameBtn.grid(row=7, column=0)

        self.originalNames = []
        self.newNames = []

        
    def browseFiles(self):
        files = filedialog.askopenfilenames(title="Select files to rename")
        print(files)
        self.originalNames = files
        self.newNames = files
        self.oldEdit.insert(INSERT, files)
        self.processNames()

    def processNames(self):
        self.newNames = self.originalNames
        self.dirName = os.path.dirname(self.originalNames[0])

        if self.prefixOn == True:
            print("prefix")
            self.newNames = [self.prefixEdit.text() + os.path.basename(x) for x in self.newNames]

        if self.suffixOn == True:
            print("suffix")
            self.newNames = [os.path.splitext(x)[0] + self.suffixEdit.text() + os.path.splitext(x)[1] for x in self.newNames ]
        
        if self.numberingOn == True:
            print("numbering")
            self.newNames = [os.path.splitext(os.path.basename(self.newNames[i]))[0] + str(i + int(self.numberingStartEdit.text())) * int(self.numberingStepEdit.text()) + os.path.splitext(os.path.basename(self.newNames[i]))[1] for (i, j) in enumerate(self.originalNames)]
        
        if self.replaceOn == True:
            print("replace")
            self.newNames = [os.path.basename(x).replace(self.replaceOldEdit.text(), self.replaceNewEdit.text()) for x in self.originalNames]

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
