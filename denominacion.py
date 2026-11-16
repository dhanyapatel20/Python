from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.configure(bg="lightblue")
root.title("Denominacion counter")
upload = Image.open("app.png")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="lightblue")

label.place(x=180, y=20)

l1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg="lightblue")
l1.place(x=180, y=340)

def msg():
    msgbox=messagebox.showinfo("Denomination Counter", "This application is designed to help you count the denominations of currency notes. Please enter the number of notes for each denomination and click 'Calculate' to see the total amount.")

    if msgbox == "ok":
        topwin()

button1 = Button(root, text="Click Here to Start", command=msg, bg="lightblue")
button1.place(x=250, y=370)

def topwin():
    top = Toplevel()
    top.geometry("650x400")
    top.configure(bg="lightgrey")
    top.title("Denomination Counter")

    label = Label(top, text="enter total amount:", bg="lightgrey")
    entry = Entry(top)

    lbl= Label(top, text="Enter the number of notes for each denomination:", bg="lightgrey")

    l1 = Label(top, text="Denomination 2000:", bg="lightgrey")
    l2 = Label(top, text="Denomination 500:", bg="lightgrey")
    l3 = Label(top, text="Denomination 100:", bg="lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())
            notes_2000 = amount // 2000
            amount %= 2000
            notes_500 = amount // 500
            amount %= 500
            notes_100 = amount // 100

            t1.delete(0, END)
            t1.insert(0, str(notes_2000))
            t2.delete(0, END)
            t2.insert(0, str(notes_500))
            t3.delete(0, END)
            t3.insert(0, str(notes_100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculate, bg="lightgrey")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)

    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)

    l2.place(x=180, y=230)

    l3.place(x=180, y=260)

    t1.place(x=270, y=200)

    t2.place(x=270, y=230)

    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()