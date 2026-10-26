from tkinter import *

window = Tk()
window.title("Event Handling")
window.geometry("100x100")

def handel_keypress(event):
    print(event.char)

window.bind("<Key>", handel_keypress)

def handel_mouse_click(event):
    print("\nthe button was clicked")

butten=Button(text="clich me")
butten.pack()

butten.bind("<Button-1>",handel_mouse_click)

window.mainloop()