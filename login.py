from tkinter import *

root = Tk()
root.title("Login")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360,bg="lightblue")

label1 = Label(master=frame, text="fullname",bg="blue",fg="white",width=12)
label2 = Label(master=frame, text="email",bg="blue",fg="white",width=12)
label3 = Label(master=frame, text="password",bg="blue",fg="white",width=12)

name_entry = Entry(master=frame)
email_entry = Entry(master=frame)
password_entry = Entry(master=frame, show="*")

def displayes():
    name = name_entry.get()
    greeting = f"Hello, {name}!"
    message="\n concraculations for your new account!"
    textbox.insert(END, greeting)
    textbox.insert(END, message)

textbox = Text(bg="lightgray", fg="black")
btn = Button(text="Create Account", command=displayes,bg="red",fg="white")

frame.place(x=20,y=0)

label1.place(x=20, y=20)

name_entry.place(x=150, y=20)

label2.place(x=20, y=80)

email_entry.place(x=150, y=80)

label3.place(x=20, y=140)

password_entry.place(x=150, y=140)

btn.place(x=130, y=210)

textbox.place(y=250)

root.mainloop()