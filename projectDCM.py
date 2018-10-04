from tkinter import *

window = Tk()
window.title("Pacemaker DCM")

lbl = Label(window, text="Sign in or create a new user account.")
lbl.grid(column=0, row=0)

window.geometry('350x200')
#open the window and await user interaction
window.mainloop()