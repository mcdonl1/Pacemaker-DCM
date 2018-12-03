import serial
import os

try:
        os.remove('readings.txt') #remove file every time you run
except WindowsError:
        pass

arduinoSerialData=serial.Serial(timeout=1,baudrate=9600)
arduinoSerialData.port='COM3'
arduinoSerialData.open()

def run_it():
	while True:
		if (str(arduinoSerialData.read(1)))!='':
			try:
			    s= arduinoSerialData.read(1)
			    with open('readings.txt', 'a') as f:
			        f.write(str(int.from_bytes(s, byteorder='big'))+'\n')
			        print (str(int.from_bytes(s, byteorder='big')))
			except IndexError:
				run_it()
		else:
			run_it()
run_it()

