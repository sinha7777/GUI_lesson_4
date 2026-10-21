from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

root = Tk()

root.geometry("200x100")
root.title("Save file")

def save_file():
    files = [("All Files","*.*"),
             ("Python Files","*.py"),
             ("Text Document","*.txt"),]
    file = asksaveasfile(filetypes=files,defaultextension=files)

b1 = Button(root,text="save",command=save_file)
b1.pack(pady=20)

root.mainloop()