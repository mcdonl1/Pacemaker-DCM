from tkinter import *
from tkinter.ttk import *
from userAuth import *
from authentication import is_valid
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

        for F in (CreateAccount, Login, MainControl, AdminPage):
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
    

    #Simple test authentication
    def testLogin(self):
        if self.usernameField.get() == "admin" and self.pwField.get() == "admin":
           self.controller.show_frame(AdminPage)
        else:
            auth = is_valid(self.usernameField.get(), self.pwField.get())
            if auth:
                self.controller.show_frame(MainControl)
            else:
                self.failureWarning.config(text="Invalid username or password.")


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
        if self.showingParams:
            self.params.pack_forget() 
        self.params = EditParams(self.container, self, data.paramArrays[mode])
        self.params.pack(side="top",fill=X, expand=False)
        self.showingParams = True
        self.controller.geometry("800x500")
        
        
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
        logoutBtn.grid(row=0, column=2, padx=90, pady=5, sticky=E)

        currentModeText = Label(self, text="Current Mode: ")
        currentModeText.grid(row=1, column=0, padx=5)
    
    #Function to tell controller to display required parameters based on mode selected
    def func(self, value):
        self.controller.showParams(value)

#A view that shows the current mode's editable parameters. Takes parent, controller and an array of params to be shown (stored in data.py)
class EditParams(Frame):
    def __init__(self, parent, controller, params):     #pass in an array of parameters to be available for edit
        Frame.__init__(self, parent)

        cvlbl = Label(self, text="Current Value")
        cvlbl.grid(row=0, column=5, sticky=E)

        #Create object properties to hold references to widgets annd values created for later access
        self.params = params
        self.dropdownValues = {}
        self.lbls = {}
        self.entries = {}
        self.spinbox = {}
        self.btns = {}
        self.currentValueDisp = {}
        self.currentValueUnits = {}

        #Loops through list of parameters and creates required entry/dropdown fields with labels and buttons as required
        #Stores createed widgets in lists inside object for later access upon user interaction
        i = 1
        for p in params:
            param = p[0]
            if(len(p) == 1): entryType = "entry"
            else: entryType = p[1]
            self.lbls[param] = Label(self, text=param+":")
            self.lbls[param].grid(column=0, row=i, sticky=W)
            if entryType == "entry":
                self.entries[param] = Entry(self, width=5)
                self.entries[param].grid(column=1, row=i, sticky=W)
                self.btns[param] = Button(self, text="Enter", command=lambda p=param: self.getEntryValue(p))
                self.btns[param].grid(column=2, row=i, sticky=W)
            elif entryType == "dropdown":
                self.dropdownValues[param] = StringVar()
                self.dropdownValues[param].set(p[2][0])
                self.entries[param] = OptionMenu(self, self.dropdownValues[param], *p[2], command=lambda v, p=param: self.getDropdownValue(v,p))
                self.entries[param].grid(column=1, row=i, sticky=W)
            elif entryType == "ranges":
                self.dropdownValues[param] = StringVar()
                self.dropdownValues[param].set(p[2][0])
                self.entries[param] = OptionMenu(self, self.dropdownValues[param], *p[2], command=lambda v, p=param, index=i: self.showSpinbox(p,index))
                self.entries[param].grid(column=1, row=i, sticky=W)
            elif entryType == "spinbox":
                self.spinbox[param] = Spinbox(self, from_=p[2], to=p[3], increment=p[4])
                self.spinbox[param].grid(column=1, row=i, sticky=W)
                self.btns[param] = Button(self, text="Enter", command=lambda p=param: self.getSpinboxValue(p))
                self.btns[param].grid(column=2, row=i, sticky=W)

            self.currentValueDisp[param] = Label(self, text=str(data.currentValues[param][0]))
            self.currentValueDisp[param].grid(column=5, row=i, padx=15, sticky=E)
            self.currentValueUnits[param] = Label(self, text=data.currentValues[param][1])
            self.currentValueUnits[param].grid(column=6, row=i, sticky=W)
            i += 1
        self.connected = PhotoImage(file="disconnected.gif")
        self.communication = Label(self, image=self.connected) #will be changed while communicating with PACEMAKER
        self.communication.photo = self.connected
        self.communication.grid(column=1, row=i, pady=50)
        self.programBtn = Button(self, text="Program", command=lambda:self.program())
        self.programBtn.grid(column=0, row=i, pady=50)
        
    #function to handle value chosen in dropdown menu
    def getDropdownValue(self, value, param):
        data.currentValues[param][0] = value
        self.updateCurrentValues()

    #function to get values from entry field when button presses
    def getEntryValue(self, param):  
        data.currentValues[param][0] = self.entries[param].get()
        self.updateCurrentValues()
    
    def getSpinboxValue(self, param):
        data.currentValues[param][0] = self.spinbox[param].get()
        self.updateCurrentValues()

    #function to show a secondary entry method for params that have different ranges of values
    def showSpinbox(self, param, index):
        paramInfo = self.params[index-1] #param info list from data file
        entryType = paramInfo[3]    #secondarry entry field
        spinMode = 0    #initialize
        if entryType == "spinbox":
            #find the index at which the info for this range's spinbox is stored
            i = 0
            for option in paramInfo[2]:
                if option == self.dropdownValues[param].get():
                    spinMode = i - 1
                i += 1
            lbl = Label(self, text="Adjust value:")
            lbl.grid(column=2, row=index)
           
            #Create spinbox using data from data.py
            #Create a button to enter the current value of the spinbo
            self.spinbox[param] = Spinbox(self, from_=paramInfo[4][spinMode][0], to=paramInfo[4][spinMode][1], increment=paramInfo[4][spinMode][2])  
            self.spinbox[param].grid(column=3, row=index)
            self.btns[param] = Button(self, text="Enter", command=lambda p=param: self.getSpinboxValue(p))
            self.btns[param].grid(column=4, row=index, sticky=W)

    def updateCurrentValues(self):
        i=1
        for p in self.params:
            param = p[0]
            self.currentValueDisp[param].grid_remove()

        for p in self.params:
            param = p[0]
            self.currentValueDisp[param] = Label(self, text=str(data.currentValues[param][0]))
            self.currentValueDisp[param].grid(column=5, row=i, padx=15, sticky=E)
            i += 1
    
    def program(self):
        for p in self.params:
            param = p[0]
            #sendValue(data.currentValues[param][0], param) #to be written (function to send a value to the PACEMAKER, will take value and parameter)
            print(param +" value=" + str(data.currentValues[param][0]) + ". Sent." )

class AdminPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lbl = Label(self, text="Admin page")
        removeUsersBtn = Button(self, text="Clear Users", command=self.remove)
        self.successMessage = Label(self, text="")

        lbl.grid(row=0, column=0, sticky=W)
        removeUsersBtn.grid(row=1, column=0, sticky=W)
        self.successMessage.grid(row=1, column=1, sticky=E)

        logoutBtn = Button(self, text="Logout", command=lambda:controller.show_frame(Login))
        logoutBtn.grid(row=0, column=1, padx=290, pady=5, sticky=E)

    def remove(self):
        clearUsers("users.txt")
        self.successMessage.config(text="Users cleared.")

#Instantiate app and change title and dimensions
app = App()
app.title("Pacemaker DCM")

app.geometry('500x350')

#open the app and await user interaction
app.mainloop()

