import serial
import matplotlib.pyplot as plt
from drawnow import *

values = []

plt.ion()
cnt=0


def plotValues():
    plt.grid(True)
    plt.plot(values)

#pre-load dummy data
for i in range(0,50):
    values.append(0)
    
while True:
    graph_data=open('readings.txt','r').read() #reads all the file at once
    lines = graph_data.split('\r\n')
    lines.pop()# removes the last element which is a whitespace
    ys = list(map(int,lines))#maps values to integer
    for _ in ys:
        values.append(_)
        values.pop(0)
        drawnow(plotValues)
            
