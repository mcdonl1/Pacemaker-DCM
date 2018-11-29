import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
frame1 = plt.gca()

plt.ylim(ymax=1050)

def animate(i):
    graph_data=open('readings.txt','r').read() #reads all the file at once
    lines = graph_data.split('\r\n')
    lines.pop()# removes the last element which is a whitespace
    
    ys = list(map(int,lines)) #maps values to integer
    xs = range(len(ys)) #creates corresp. indexs
    ax1.clear() #color black

    frame1.axes.xaxis.set_ticklabels([])#remove labels from x axis
    ax1.relim()
    ax1.autoscale_view()

    plt.plot(ys)
    

ani = animation.FuncAnimation(fig, animate,interval=1000)

def showPlot():
    plt.show()
