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
        self.usernameField = Entry(self, width=20)
        self.pwField = Entry(self, width=20, show="*")
        self.cpwField = Entry(self, width=20, show="*")
        createAccountBtn = Button(self, text="Create Account", command=self.addUserHelper)
        self.successMessage = Label(self, text = "")


        #design
        usernameLbl.grid(column=0,row=3, sticky=W)
        pwLbl.grid(column=0,row=4, sticky=W)
        cpwLbl.grid(column=0,row=5, sticky=W)
        self.usernameField.grid(column=1,row=3, sticky=E)
        self.pwField.grid(column=1,row=4, sticky=E)
        self.cpwField.grid(column=1, row=5, sticky=E)
        createAccountBtn.grid(column=1, row=6, sticky=E)
        self.successMessage.grid(column=1, row=7, sticky=E)

    def addUserHelper(self):
        pw = self.pwField.get()
        cpw = self.cpwField.get()
        user = self.usernameField.get()
        print(pw)
        if pw == cpw and pw != "":
            addUser("users.txt", user, pw, cpw)
            self.successMessage.config(text="Success! Please log in.")
        elif pw != cpw:
            self.successMessage.config(text="Passwords must match.")
        elif pw == "" or cpw == "" or user == "":
            self.successMessage.config(text="All fields are required.")
        else:
            self.successMessage.config(text="Failed: Please try again.")


            
#Login screen
class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        createAcctScreenBtn = Button(self, text="Create Account", command=lambda:controller.show_frame(CreateAccount))
        loginScreenBtn = Button(self, text="Login", command=lambda:controller.show_frame(Login))
        createAcctScreenBtn.grid(row=1, column=0,padx=5, pady=5)
        loginScreenBtn.grid(row=1, column=1,padx=5, pady=5)

        lbl = Label(self, text="Login to your account.")
        lbl.grid(row=0, column=1, padx=10, pady=10)

        #components
        usernameLbl = Label(self, text="Username:")
        pwLbl = Label(self, text="Password:")
        self.usernameField = Entry(self, width=20)
        self.pwField = Entry(self, width=20, show="*")
        LoginBtn = Button(self, text="Login", command=self.testLogin) #command to be changed to auth() once authentication is functional
        self.failureWarning = Label(self, text="")

        #design
        usernameLbl.grid(column=0,row=3, sticky=W)
        pwLbl.grid(column=0,row=4, sticky=W)
        self.usernameField.grid(column=1,row=3, sticky=E)
        self.pwField.grid(column=1,row=4, sticky=E)
        LoginBtn.grid(column=1, row=6, sticky=E)
        self.failureWarning.grid(column=1, row=7, sticky=E)
    
    def auth(self):
        return True
        #if login is successful, change to ModeSelect

    #Simple test authentication
    def testLogin(self):
        if self.usernameField.get() == "test" and self.pwField.get() == "password":
            self.controller.show_frame(MainControl)
        else:
            self.failureWarning.config(text="Try again.")


class MainControl(Frame):       #main control view of DCM - contains a mode selector and fields for editting parameters
    def __init__(self, parent, controller):
        #Pass contoller down
        self.controller = controller;
        Frame.__init__(self, parent)
        #configure container to hold mode selection and parameter edit screen
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.showingParams = False #at first no params are showing

        select = ModeSelect(self.container, self)       #Instantiate mode selector widget
        select.pack(side="top",fill=X, expand=False)

    #Function to show parameter selection screen based on which mode has been selected in the mode dropdown
    def showParams(self,mode):
        #If params are showing, clear them and show newly selected mode's params
        if(self.showingParams):
            self.params.pack_forget() 
        self.params = EditParams(self.container, self, data.paramArrays[mode])
        self.params.pack(side="top",fill=X, expand=False)
        self.showingParams = True
        
        
#A view that allows the user to select their required mode of operation, which then triggers the required parameters to be displayed and editable
class ModeSelect(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #The intial value for the dropdown menu
        self.initValue = StringVar() 
        self.initValue.set("Select a Mode")

        #Pass controller to object for later use
        self.controller=controller


        lbl = Label(self, text="Select operating mode: ")
        dropdown = OptionMenu(self, self.initValue, *data.modes, command=self.func)
        
        lbl.grid(row=0, column=0)
        dropdown.grid(row=1,column=1, sticky=W)

        #Simple logout button that returns user to login screen upon press
        logoutBtn = Button(self, text="Logout", command=lambda:controller.controller.show_frame(Login))
        logoutBtn.grid(row=0, column=1, padx=290, pady=5, sticky=E)

        currentModeText = Label(self, text="Current Mode: ")
        currentModeText.grid(row=1, column=0, padx=5)
    
    #Function to tell controller to display required parameters based on mode selected
    def func(self, value):
        self.controller.showParams(value)

#A view that shows the current mode's editable parameters. Takes parent, controller and an array of params to be shown (stored in data.py)
class EditParams(Frame):
    def __init__(self, parent, controller, params):     #pass in an array of parameters to be available for edit
        Frame.__init__(self, parent)

        #Create object properties to hold references to widgets created for later access
        self.params = params
        self.lbls = {}
        self.entries = {}
        self.btns = {}

        #Loops through list of parameters and creates required entry/dropdown fields with labels and buttons as required
        #Stores createed widgets in lists inside object for later access upon user interaction
        i = 0
        for p in params:
            param = p[0]
            if(len(p) == 1): entryType = "entry"
            else: entryType = p[1]
            self.lbls[param] = Label(self, text=param+":")
            self.lbls[param].grid(column=0, row=i, sticky=W)
            if entryType == "entry":
                self.entries[param] = Entry(self, width=5)
                self.entries[param].grid(column=1, row=i, sticky=W)
                self.btns[param] = Button(self, text="Enter", command=lambda p=param: self.func(p))
                self.btns[param].grid(column=2, row=i, sticky=W)
            elif entryType == "dropdown":
                self.default = StringVar()
                self.default.set(p[2][0])
                self.entries[param] = OptionMenu(self, self.default, *p[2], command=self.dropdownValue)
                self.entries[param].grid(column=1, row=i, sticky=W)
            i += 1

    #function to handle value chosen in dropdown menu
    def dropdownValue(self, value):
        print(value)

    #function to get values from entry field when button presses
    def func(self, value):  
        param = self.entries[value].get()
        print(param)

#Instantiate app and change title and dimensions
app = App()
app.title("Pacemaker DCM")

app.geometry('500x350')

#open the app and await user interaction
app.mainloop()

