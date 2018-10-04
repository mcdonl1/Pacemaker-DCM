from tkinter import *

#Initialize window
window = Tk()
window.title("Pacemaker DCM")

lbl = Label(window, text="Sign in or create a new user account.")
lbl.grid(column=1, row=0)

window.geometry('700x500')

#Screen placeholders
screenPlaceholder = Label(window, text="Create Account Screen")
screenPlaceholder.grid(column=1, row=3)

showCreateAcctScreen = True #If false, show login screen


#Select screen
def showCreateAcct():
    screenPlaceholder.configure(text="Create Account Screen")
    showCreateAcctScreen = True

def showLogin():
    screenPlaceholder.configure(text="Login Screen")
    showCreateAcctScreen = False

createAcctBtn = Button(window, text="Create Account", command=showCreateAcct)
loginBtn = Button(window, text="Login", command=showLogin)
createAcctBtn.grid(column=0, row=1)
loginBtn.grid(column=1, row=1)

#Create



#open the window and await user interaction
window.mainloop()

