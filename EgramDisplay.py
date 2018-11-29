
#tkinter and project imports
from tkinter import *
from tkinter.ttk import *
import data as data
import serial
import projectDCM as proj
from serialgraphing import live_graph as graph

#Matplotlib imports
import matplotlib
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

#Graph display class
class EgramDisplay(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Graph Page", font=26)
        label.pack(pady=10,padx=10)

        showPlotButton= Button(self, text="Show Electrogram", command=lambda: graph.showPlot())
        showPlotButton.pack()

        button1 = Button(self, text="Back to Dashboard",command=lambda: controller.show_frame(proj.MainControl))
        button1.pack()
        