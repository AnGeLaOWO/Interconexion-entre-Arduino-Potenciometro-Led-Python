import serial 
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib.lines import Line2D
import numpy as np
from sympy import Interval, intervals 

def getSerialData(self, Samples, numData, serialConnection, lines):
    for i in range(numData) :
        value = float(serialConnection.readline().strip())
        data[i].append(value)
        lines[i].set_data(range(Samples), data[i])
        
serialPort = 'COM6'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except:
    print('Cannot conect to the port')
    
Samples = 200
sampleTime = 100
numData = 1

xmin = 0
xmax = Samples
ymin = 0
ymax = 6
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen = Samples))
    lines.append(Line2D([], [], color='blue'))
    
fig = plt.figure()
axl = fig.add_subplot(1, 1, 1, xlim=(xmin, xmax), ylim=(ymin, ymax))
axl.title.set_text('First Plot')
axl.set_xlabel("Samples")
axl.set_ylabel("volts")
axl.add_line(lines[0])
    
    
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval = sampleTime)
plt.show()
    
serialConnection.close()
