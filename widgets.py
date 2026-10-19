from tkinter import *
from datetime import date

root = Tk()
root.title("tkinter widgets")
root.geometry("500x500")

lbl = Label(root, text="hey there!", fg="white", bg="black",height=1, width=20)

name_label = Label(root, text="full Name",bg="red", fg="blue")

name_entery=Entry()

def desplay():
    name = name_entery.get()
    global mesage
    mesage = "welcome to the eplecation \n today date is"
    greet="Hello, " + name + "!"
    textbox.insert(END, mesage)
    textbox.insert(END, greet)
    textbox.insert(END, date.today())

textbox = Text(root, height=3) 

ben = Button(root, text="click me", command=desplay)

lbl.pack()
name_label.pack()
name_entery.pack()
ben.pack()
textbox.pack()

root.mainloop()
