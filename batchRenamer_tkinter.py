from tkinter import INSERT, Tk, Frame, Button, Entry, Checkbutton, Text, IntVar, filedialog, messagebox

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
        self.oldNames.grid(row=1, column=0, columnspan=4)
        
        prefixOn = IntVar()
        self.prefixChkbox = Checkbutton(self, text="prefix", variable=prefixOn) 
        self.prefixChkbox.grid(row=2, column=0)
        self.prefixEdit = Entry(self)
        self.prefixEdit.grid(row=2, column=1)

        suffixOn = IntVar()
        self.suffixChkbox = Checkbutton(self, text="suffix", variable=suffixOn)
        self.suffixChkbox.grid(row=3, column=0) 
        self.suffixEdit = Entry(self)
        self.suffixEdit.grid(row=3, column=1)

        numberingOn = IntVar()
        self.numberingChkbox = Checkbutton(self, text="numbering", variable=numberingOn)
        self.numberingChkbox.grid(row=4, column=0) 
        self.numberingStartEdit = Entry(self)
        self.numberingStartEdit.grid(row=4, column=1)
        self.numberingStepEdit = Entry(self)
        self.numberingStepEdit.grid(row=4, column=2)

        replaceOn = IntVar()
        self.replaceChkbox = Checkbutton(self, text="replace", variable=replaceOn)
        self.replaceChkbox.grid(row=5, column=0) 
        self.replaceOldEdit = Entry(self)
        self.replaceOldEdit.grid(row=5, column=1)
        self.replaceNewEdit = Entry(self)
        self.replaceNewEdit.grid(row=5, column=2)
        
        self.renameBtn = Button(self, text="rename", command=self.confirm)
        self.renameBtn.grid(row=6, column=0)

        
    def browseFiles(self):
        files = filedialog.askopenfilenames(title="Select files to rename")
        print(files)
        self.oldNames.insert(INSERT, files)

    def confirm(self):
        messagebox.askyesno('Confirm file rename', 'Rename files ?')


root = Tk()
root.title('Batch Renamer')
root.geometry("620x500")

app = batchRenamer(root)

root.mainloop()
root.destroy()
