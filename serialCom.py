
import serial
import data

START_CODE = 16
REQ_PACE_PARAMS_CODE = 22
SEND_PACE_PARAMS_CODE = 55
EGRAM_CODE = 33


serialObj = serial.Serial(timeout=1,baudrate=115200)
serialObj.port='COM3'
txEnable = False #True if transmitting
rxEnable = False #True if receiving
serialObj.open()


def endComs():
	rxEnable = False
	txEnable = False

def closeComs():
	serialObj.close()

def serializeData(dataVal, sign, byteLen):
	'serializes a into appropriate amount of bytes using Big-Endian.'
	#print(byteLen,int((byteLen/8))) #remove me later XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	return dataVal.to_bytes(byteLen, byteorder='big', signed=sign)

def transmit(comType):
	'transmits data based on comType requested'
	if (txEnable == True):
		serialObj.write(START_CODE)

		if (comType == 'sendParams'):
			serialObj.write(serializeData(SEND_PACE_PARAMS_CODE,False,1)) #begin params transmission
			params = data.currentValues
			
			modeNum = index(data.modes["mode"])
			serial.write(serializeData(modeNum,False,1));

			#Serialize and send params 
			for k in params.keys():
				if (k=='mode'):
					continue #skip mode since that was already done above
				if (k=="Lower Rate Limit" or k=="Upper Rate Limit" or k== 'Maximum Sensor Rate' or k== 'Dynamic AV Delay'  or k== 'Rate Smoothing' or k== 'ATR Mode' or k== 'ATR Fallback Time' or k== 'Response Time' or k== 'Response Factor' or k== 'Recovery Time'): #unsigned 8 bit ints
					serial.write(serializeData(params[k],False,1));
				if (k== 'Fixed AV Delay' or k == 'Ventricular Refactory Period' or k == 'PVARP' or k == 'Atrial Refactory Period' or k == 'PVARP Extension' or k == 'ATR Duration'):
					serial.write(serializeData(params[k],False,2));
				if(k== 'Sensed AV Delay Offset'):
					serial.write(serializeData(params[k],True,1));
				else: #singles 
					serial.write(serializeData(params[k],True,4))

			serialObj.write(serializeData(SEND_PACE_PARAMS_CODE,False,1)) #end params transmission
			
			txEnable = False

			rxEnable = True
			receivedParams = receiveParams(comType)	#receive parameters
			#verify parameters

		if (comType == 'egram'):
			serialObj.write(serializeData(EGRAM_CODE,False,1))
			txEnable = False
			rxEnable = True
			receive(comType)

		txEnable = False


def receive(comType):
	'reads incoming serial data'

	started = False
	while (rxEnable):
		readData = serialObj.readline()
		print('Reading', readData, hex(int.from_bytes(readData, byteorder='big', signed=False)))			#remove me later XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
		if (comType != 'egram' or comType != 'receiveParams'):
			rxEnable = False
		if (int.from_bytes(readData, byteorder='big', signed=False) == 16): #start code detected
			started = True

		storedParams = []
		if (started):
			if (comType == 'egram'):
				pass #keep reading and display on plot
			elif (comType == 'receiveParams'):
				storedParams.append(readData)

	return storedParams #return received parameters













