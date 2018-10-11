from tkinter import *
from tkinter.ttk import *
from userAuth import *

#Initialize Window class
class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (CreateAccount, Login):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(CreateAccount)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class CreateAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        createAcctScreenBtn = Button(self, text="Create Account", command=lambda:controller.show_frame(CreateAccount))
        loginScreenBtn = Button(self, text="Login", command=lambda:controller.show_frame(Login))
        createAcctScreenBtn.grid(row=1, column=0,padx=5, pady=5)
        loginScreenBtn.grid(row=1, column=1,padx=5, pady=5)

        lbl = Label(self, text="Create a new user account.")
        lbl.grid(row=0, column=1, padx=10, pady=10)

        #components
        usernameLbl = Label(self, text="Username:")
        pwLbl = Label(self, text="Password:")
        cpwLbl = Label(self, text="Confirm Password:")
        usernameField = Entry(self, width=20)
        pwField = Entry(self, width=20)
        cpwField = Entry(self, width=20)
        createAccountBtn = Button(self, text="Create Account", command=addUser("users.txt",usernameField.get(), pwField.get(), cpwField.get()))

        #design
        usernameLbl.grid(column=0,row=3)
        pwLbl.grid(column=0,row=4)
        cpwLbl.grid(column=0,row=5)
        usernameField.grid(column=1,row=3)
        pwField.grid(column=1,row=4)
        cpwField.grid(column=1, row=5)
        createAccountBtn.grid(column=1, row=6)

class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        createAcctScreenBtn = Button(self, text="Create Account", command=lambda:controller.show_frame(CreateAccount))
        loginScreenBtn = Button(self, text="Login", command=lambda:controller.show_frame(Login))
        createAcctScreenBtn.grid(row=1, column=0,padx=5, pady=5)
        loginScreenBtn.grid(row=1, column=1,padx=5, pady=5)

        lbl = Label(self, text="Login to your account.")
        lbl.grid(row=0, column=1, padx=10, pady=10)

        #components
        usernameLbl = Label(self, text="Username:")
        pwLbl = Label(self, text="Password:")
        usernameField = Entry(self, width=20)
        pwField = Entry(self, width=20)
        LoginBtn = Button(self, text="Login")

        #design
        usernameLbl.grid(column=0,row=3)
        pwLbl.grid(column=0,row=4)
        usernameField.grid(column=1,row=3)
        pwField.grid(column=1,row=4)
        LoginBtn.grid(column=1, row=6)
            

    


    
        
        
        # createAcctScreenBtn = Button(self, text="Create Account", command=show_frame(CreateAccount))
        # loginScreenBtn = Button(self, text="Login", command=show_frame(Login))

        # createAcctScreenBtn.place(x=0,y=1*lineheight)
        # loginScreenBtn.place(x=120,y=1*lineheight)

        # usernameLbl = Label(self, text="Username:")
        # pwLbl = Label(self, text="Password:")
        # cpwLbl = Label(self, text="Confirm Password:")
        # usernameField = Entry(self, width=20)
        # pwField = Entry(self, width=20)
        # cpwField = Entry(self, width=20)
        # createAccountBtn = Button(self, text="Create Account")

        # usernameLbl.place(x=0,y=2*lineheight)
        # pwLbl.place(x=0,y=3*lineheight)
        # cpwLbl.place(x=0,y=4*lineheight)
        # usernameField.place(x=120,y=2*lineheight)
        # pwField.place(x=120,y=3*lineheight)
        # cpwField.place(x=120,y=4*lineheight)
        # createAccountBtn.place(x=120,y=5*lineheight)


app = App()
app.title("Pacemaker DCM")

app.geometry('700x500')


# showCreateAcctScreen = True #If false, show login screen


# #Select screen
# def showCreateAcct():
#     showCreateAcctScreen = True

# def showLogin():
#     showCreateAcctScreen = False

# createAcctScreenBtn = Button(self, text="Create Account", command=showCreateAcct)
# loginScreenBtn = Button(self, text="Login", command=showLogin)
# createAcctScreenBtn.grid(column=0, row=1)
# loginScreenBtn.grid(column=1, row=1)

# #Create Account Screen
# if showCreateAcctScreen:
#     #components
#     usernameLbl = Label(self, text="Username:")
#     pwLbl = Label(self, text="Password:")
#     cpwLbl = Label(self, text="Confirm Password:")
#     usernameField = Entry(self, width=20)
#     pwField = Entry(self, width=20)
#     cpwField = Entry(self, width=20)
#     createAccountBtn = Button(self, text="Create Account")

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
#     usernameLbl = Label(self, text="Username:")
#     pwLbl = Label(self, text="Password:")
#     usernameField = Entry(self, width=20)
#     pwField = Entry(self, width=20)
#     loginBtn = Button(self, text="Login")

#     #design
#     usernameLbl.grid(column=0,row=3)
#     pwLbl.grid(column=0,row=4)
#     usernameField.grid(column=1,row=3)
#     pwField.grid(column=1,row=4)
#     loginBtn.grid(column=1, row=5)

#open the app and await user interaction
app.mainloop()

