from tkinter import*
from tkinter import messagebox

root = Tk()

root.geometry("100x100")
root.title("Message box")

label = Label(root,text="Hello")
label.pack()

messagebox.showinfo("showinfo","It is not snowing here")

messagebox.showwarning("showwarning","Please slow down")

messagebox.showerror("showerror","Error 1982B")

messagebox.askquestion("askquestion","Are you sure?")

messagebox.askokcancel("asktocancle","Do you want to cancle?")

messagebox.askyesno("askyesorno","Is it night time?")

messagebox.askyesnocancel("askyesornocancle","Try again?")

root.mainloop()