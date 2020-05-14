import tkinter as tk
from tkinter import filedialog

class batchRenamer:

    def __init__(self, master):
        

        # window = tk.Tk()
        # window.title("File Renamer")

        frame = tk.Frame(master)
        frame.pack()
        

        self.quitBtn = tk.Button(frame, text="quit", fg="red", command=frame.quit)
        self.quitBtn.pack(side=tk.LEFT)

        self.browseBtn = tk.Button(frame, text="select files", command=self.browseFiles)
        self.browseBtn.pack(side=tk.LEFT)


    def browseFiles(self):
        files = tk.filedialog.askopenfilenames(title="Select files to rename")
        print(files)

root = tk.Tk()
root.title('Batch Renamer')

app = batchRenamer(root)

root.mainloop()
root.destroy()
