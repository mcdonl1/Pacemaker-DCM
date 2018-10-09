from tkinter import *

lineheight = 27

#Initialize Window class
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        #set title of master
        self.master.title("Pacemaker DCM")

        #allow widget to take full space of root window
        self.pack(fill=BOTH, expand=1)


        lbl = Label(root, text="Sign in or create a new user account.")
        lbl.place(x=0, y=0)

        def showLogin():
            print("Show Login")
            #show login screen

        def showCreateAcct():
            print("Show create account")
            #show create account screen

        createAcctScreenBtn = Button(root, text="Create Account", command=showCreateAcct)
        loginScreenBtn = Button(root, text="Login", command=showLogin)

        createAcctScreenBtn.place(x=0,y=1*lineheight)
        loginScreenBtn.place(x=120,y=1*lineheight)

        usernameLbl = Label(root, text="Username:")
        pwLbl = Label(root, text="Password:")
        cpwLbl = Label(root, text="Confirm Password:")
        usernameField = Entry(root, width=20)
        pwField = Entry(root, width=20)
        cpwField = Entry(root, width=20)
        createAccountBtn = Button(root, text="Create Account")

        usernameLbl.place(x=0,y=2*lineheight)
        pwLbl.place(x=0,y=3*lineheight)
        cpwLbl.place(x=0,y=4*lineheight)
        usernameField.place(x=120,y=2*lineheight)
        pwField.place(x=120,y=3*lineheight)
        cpwField.place(x=120,y=4*lineheight)
        createAccountBtn.place(x=120,y=5*lineheight)

root = Tk()
app = Window(root)

root.geometry('700x500')


# showCreateAcctScreen = True #If false, show login screen


# #Select screen
# def showCreateAcct():
#     showCreateAcctScreen = True

# def showLogin():
#     showCreateAcctScreen = False

# createAcctScreenBtn = Button(root, text="Create Account", command=showCreateAcct)
# loginScreenBtn = Button(root, text="Login", command=showLogin)
# createAcctScreenBtn.grid(column=0, row=1)
# loginScreenBtn.grid(column=1, row=1)

# #Create Account Screen
# if showCreateAcctScreen:
#     #components
#     usernameLbl = Label(root, text="Username:")
#     pwLbl = Label(root, text="Password:")
#     cpwLbl = Label(root, text="Confirm Password:")
#     usernameField = Entry(root, width=20)
#     pwField = Entry(root, width=20)
#     cpwField = Entry(root, width=20)
#     createAccountBtn = Button(root, text="Create Account")

#     #design
#     usernameLbl.grid(column=0,row=3)
#     pwLbl.grid(column=0,row=4)
#     cpwLbl.grid(column=0,row=5)
#     usernameField.grid(column=1,row=3)
#     pwField.grid(column=1,row=4)
#     cpwField.grid(column=1, row=5)
#     createAccountBtn.grid(column=1, row=6)
# else:
#     #components
#     usernameLbl = Label(root, text="Username:")
#     pwLbl = Label(root, text="Password:")
#     usernameField = Entry(root, width=20)
#     pwField = Entry(root, width=20)
#     loginBtn = Button(root, text="Login")

#     #design
#     usernameLbl.grid(column=0,row=3)
#     pwLbl.grid(column=0,row=4)
#     usernameField.grid(column=1,row=3)
#     pwField.grid(column=1,row=4)
#     loginBtn.grid(column=1, row=5)

#open the root and await user interaction
root.mainloop()

