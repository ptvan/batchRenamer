from tkinter import INSERT, END, Tk, Frame, Button, Entry, Checkbutton, Text, IntVar, filedialog, messagebox
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
        self.prefixChkbox = Checkbutton(self, text="prefix", variable=self.prefixOn, command=self.processNames) 
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
        self.oldEdit.delete(1.0, END)
        self.newEdit.delete(1.0, END)
        # print(files)
        self.originalNames = files
        self.newNames = files
        for i in range(len(files)):
            self.oldEdit.insert(INSERT, os.path.basename(files[i]))
            self.oldEdit.insert(INSERT, "\n")
        self.processNames()

    def processNames(self):
        self.newNames = self.originalNames
        self.dirName = os.path.dirname(self.originalNames[0])
        self.newEdit.delete(1.0, END)
        
        if self.prefixOn.get() == True:
            print("prefix")
            self.newNames = [self.prefixEdit.get() + os.path.basename(x) for x in self.newNames]
            print(self.newNames)

        if self.suffixOn.get() == True:
            print("suffix")
            self.newNames = [os.path.splitext(x)[0] + self.suffixEdit.get() + os.path.splitext(x)[1] for x in self.newNames ]
        
        if self.numberingOn == True:
            print("numbering")
            self.newNames = [os.path.splitext(os.path.basename(self.newNames[i]))[0] + str(i + int(self.numberingStartEdit.get())) * int(self.numberingStepEdit.get()) + os.path.splitext(os.path.basename(self.newNames[i]))[1] for (i, j) in enumerate(self.originalNames)]
        
        if self.replaceOn == True:
            print("replace")
            self.newNames = [os.path.basename(x).replace(self.replaceOldEdit.get(), self.replaceNewEdit.get()) for x in self.originalNames]

        for i in range(len(self.newNames)):
            short = os.path.basename(self.newNames[i])
            # print(short)
            self.newEdit.insert(INSERT, short)
            self.newEdit.insert(INSERT, "\n")

    def confirm(self):
        messagebox.askyesno('Confirm file rename', 'Rename files ?')
    
    def renameFiles(self):
        print("renaming files!")
        for i in range(len(self.newNames)):
            cmd = 'mv ' + self.originalNames[i] + " " + self.dirName + "/" + self.newNames[i]
            # print(cmd)
            os.system(cmd)


root = Tk()
root.title('Batch Renamer')
root.geometry("620x500")

app = batchRenamer(root)

root.mainloop()
root.quit()
