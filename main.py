from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

root = Tk()

root.geometry("200x100")
root.title("file reading")

def open_file():
    file = askopenfile(mode="r")
    if file:
        content = file.read()
        print(content)

b1 = Button(root,text="open", command=open_file)
b1.pack(pady=20)


root.mainloop()