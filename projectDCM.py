from tkinter import *
from tkinter.ttk import *
from userAuth import *

#App class - top level controller for gui
class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)


        #Instantiate each frame and assign it to the frame array in the app object
        self.frames = {}

        for F in (CreateAccount, Login):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Initially show the create account screen
        self.show_frame(CreateAccount)

    #function to show a given frame (context)
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

#Frame objects - each view in GUI is object which is shown by the app object
#Eventually moved to seperate file?
#Create account screen
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

#Login screen
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

#Instantiate app and change title and dimensions
app = App()
app.title("Pacemaker DCM")

app.geometry('700x500')

#open the app and await user interaction
app.mainloop()

