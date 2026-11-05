from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def top_win():
    top = Toplevel()
    top.geometry("180x100")
    top.title("top level")
    label = Label(top, text="This is a top level window")
    label.pack()
    top.mainloop()

l1=Label(root, text="This is the main window")
dtn=Button(root, text="Open Top Level Window", command=top_win)

l1.pack()
dtn.pack()

root.mainloop()