import serial
import os

try:
        os.remove('readings.txt') #remove file every time you run
except WindowsError:
        pass

arduinoSerialData=serial.Serial(timeout=1,baudrate=9600)
arduinoSerialData.port='COM7'
arduinoSerialData.open()

def run_it():
	while True:
		if (str(arduinoSerialData.readline()))!='':
			try:
			    s= arduinoSerialData.readline()
			    with open('readings.txt', 'a') as f:
			        f.write(s)
			        print (s)
			except IndexError:
				run_it()
		else:
			run_it()
run_it()

