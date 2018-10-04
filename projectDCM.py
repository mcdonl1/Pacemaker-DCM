from tkinter import *

#Initialize window
window = Tk()
window.title("Pacemaker DCM")

lbl = Label(window, text="Sign in or create a new user account.")
lbl.grid(column=1, row=0)

window.geometry('700x500')


showCreateAcctScreen = True #If false, show login screen


#Select screen
def showCreateAcct():
    showCreateAcctScreen = True

def showLogin():
    showCreateAcctScreen = False

createAcctScreenBtn = Button(window, text="Create Account", command=showCreateAcct)
loginScreenBtn = Button(window, text="Login", command=showLogin)
createAcctScreenBtn.grid(column=0, row=1)
loginScreenBtn.grid(column=1, row=1)

#Create Account Screen
if showCreateAcctScreen:
    #components
    usernameLbl = Label(window, text="Username:")
    pwLbl = Label(window, text="Password:")
    cpwLbl = Label(window, text="Confirm Password:")
    usernameField = Entry(window, width=20)
    pwField = Entry(window, width=20)
    cpwField = Entry(window, width=20)
    createAccountBtn = Button(window, text="Create Account")

    #design
    usernameLbl.grid(column=0,row=3)
    pwLbl.grid(column=0,row=4)
    cpwLbl.grid(column=0,row=5)
    usernameField.grid(column=1,row=3)
    pwField.grid(column=1,row=4)
    cpwField.grid(column=1, row=5)
    createAccountBtn.grid(column=1, row=6)
else:
    #components
    usernameLbl = Label(window, text="Username:")
    pwLbl = Label(window, text="Password:")
    usernameField = Entry(window, width=20)
    pwField = Entry(window, width=20)
    loginBtn = Button(window, text="Login")

    #design
    usernameLbl.grid(column=0,row=3)
    pwLbl.grid(column=0,row=4)
    usernameField.grid(column=1,row=3)
    pwField.grid(column=1,row=4)
    loginBtn.grid(column=1, row=5)

#open the window and await user interaction
window.mainloop()

