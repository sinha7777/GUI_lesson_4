from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("400x400")
root.title("Library Management")

label1 = Label(root, text="Library Management")
label1.pack()

label2 = Label(root, text="Book Name")
label2.pack()

entry1 = Entry(root)
entry1.pack()

label3 = Label(root, text="Quantity")
label3.pack()

spin1 = Spinbox(root, from_=1, to=10)
spin1.pack()

progress = Progressbar(root, length=200)
progress.pack()
progress["value"] = 0

frame1 = Frame(root)
frame1.pack()

scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=Y)

listbox1 = Listbox(frame1, yscrollcommand=scroll.set)
listbox1.pack(side=LEFT)

scroll.config(command=listbox1.yview)

listbox1.insert(END, "harry potter")
listbox1.insert(END, "percy jackson")
listbox1.insert(END, "matilda")
listbox1.insert(END, "the hobbit")
listbox1.insert(END, "diary of a wimpy kid")

button1 = Button(root, text="Add Book")
button1.pack()

button2 = Button(root, text="Remove Book")
button2.pack()

root.mainloop()