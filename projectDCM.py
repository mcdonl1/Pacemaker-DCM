from tkinter import *
from tkinter.ttk import *
from userAuth import *
import data as data

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

        for F in (CreateAccount, Login, MainControl):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Initially show the create account screen
        self.show_frame(CreateAccount)
        #self.show_frame(ModeSelect)

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
        lbl.grid(row=0, column=1, pady=10)

        #components
        usernameLbl = Label(self, text="Username:")
        pwLbl = Label(self, text="Password:")
        cpwLbl = Label(self, text="Confirm Password:")
        usernameField = Entry(self, width=20)
        pwField = Entry(self, width=20)
        cpwField = Entry(self, width=20)
        createAccountBtn = Button(self, text="Create Account", command=addUser("users.txt",usernameField.get(), pwField.get(), cpwField.get()))

        #design
        usernameLbl.grid(column=0,row=3, sticky=W)
        pwLbl.grid(column=0,row=4, sticky=W)
        cpwLbl.grid(column=0,row=5, sticky=W)
        usernameField.grid(column=1,row=3, sticky=E)
        pwField.grid(column=1,row=4, sticky=E)
        cpwField.grid(column=1, row=5, sticky=E)
        createAccountBtn.grid(column=1, row=6, sticky=E)

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
        LoginBtn = Button(self, text="Login", command=lambda:controller.show_frame(MainControl)) #command to be changed to auth() once authentication is functional

        #design
        usernameLbl.grid(column=0,row=3, sticky=W)
        pwLbl.grid(column=0,row=4, sticky=W)
        usernameField.grid(column=1,row=3, sticky=E)
        pwField.grid(column=1,row=4, sticky=E)
        LoginBtn.grid(column=1, row=6, sticky=E)
    
    def auth(self):
        return True
        #if login is successful, change to ModeSelect
class MainControl(Frame):
    def __init__(self, parent, controller):
        self.controller = controller;
        Frame.__init__(self, parent)
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        select = ModeSelect(self.container, self)
        select.pack(side="top",fill=X, expand=False)

    def showParams(self,mode):
        params = EditParams(self.container, self, data.paramArrays[mode])
        params.pack(side="top",fill=X, expand=False)
        

class ModeSelect(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.initValue = StringVar() 
        self.initValue.set("Select a Mode")

        self.controller=controller


        lbl = Label(self, text="Select operating mode: ")
        dropdown = OptionMenu(self, self.initValue, *data.modes, command=self.func)
        
        lbl.grid(row=0, column=0)
        dropdown.grid(row=1,column=1, sticky=W)

        logoutBtn = Button(self, text="Logout", command=lambda:controller.controller.show_frame(Login))
        logoutBtn.grid(row=0, column=1, padx=290, pady=5, sticky=E)

        currentModeText = Label(self, text="Current Mode: ")
        currentModeText.grid(row=1, column=0, padx=5)
    
    def func(self, value):
        self.controller.showParams(value)

class EditParams(Frame):
    def __init__(self, parent, controller, params):     #pass in an array of parameters to be available for edit
        Frame.__init__(self, parent)
        self.params = params
        i = 0
        for p in params:
            Label(self, text=params[i]+":").grid(column=0, row=i, sticky=W)
            Entry(self, width=5).grid(column=1, row=i, sticky=W)
            Button(self, text="Enter").grid(column=2, row=i, sticky=W)
            i += 1



#Instantiate app and change title and dimensions
app = App()
app.title("Pacemaker DCM")

app.geometry('500x350')

#open the app and await user interaction
app.mainloop()

