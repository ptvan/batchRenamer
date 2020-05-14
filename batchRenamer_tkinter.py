import tkinter as tk
from tkinter import filedialog

class batchRenamer:

    def __init__(self, master):
        

        # window = tk.Tk()
        # window.title("File Renamer")

        frame = tk.Frame(master)
        frame.pack()
        

        self.button = tk.Button(frame, text="quit", fg="red", command=frame.quit)
        self.button.pack(side=tk.LEFT)

        self.browseBtn = tk.Button(frame, text="select files", command=self.browseFiles)
        self.browseBtn.pack(side=tk.LEFT)


    def browseFiles(self):
        return tk.filedialog.askopenfile(mode="r")

root = tk.Tk()
root.title('Batch Renamer')

app = batchRenamer(root)

root.mainloop()
root.destroy()
