modes = [
            "Select a Mode",
            "AAT",
            "VVT",
            "AOO",
            "AAI",
            "VOO",
            "VVI",
            "VDD",
            "DOO",
            "DDI",
            "DDD",
            "AOOR",
            "AAIR",
            "VOOR",
            "VVIR",
            "VDDR",
            "DOOR",
            "DDIR",
            "DDDR"
        ]
#Each mode's parameters and their method of input
#for dropdown menu, need to specify list of options

#Entry - [Param]
#Dropdown - [Param, "dropdown", [options]]
#Spinbox - [Param, "spinbox", from, to, increment]

paramArrays = {   
            "AAT": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]], ["Upper Rate Limit", "spinbox", 50, 175, 5], ["Atrial Amplitude", "dropdown", ["Opt 1", "Opt 2"]], ["Atrial Pulse Width"], ["Atrial Sensitivity"], ["Atrial Refractory Period"], ["PVARP"]],
            "VVT": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]], ["Upper Rate Limit", "spinbox", 50, 175, 5], ["Atrial Amplitude"], ["Atrial Pulse Width"]],
            "AOO": [],
            "AAI": [],
            "VOO": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]], #need to add selector for Lower Rate Limit value
            "VVI": [],
            "VDD": [],
            "DOO": [],
            "DDI": [],
            "DDD": [],
            "AOOR": [],
            "AAIR": [],
            "VOOR": [],
            "VVIR": [],
            "VDDR": [],
            "DOOR": [],
            "DDIR": [],
            "DDDR": []
}

#stores current values of each parameter - modified by parameter edit screen each time a parameter is changed
currentValues = {
    "Mode": "DDD",
    "Lower Rate Limit": 60,
    "Upper Rate Limit": 120,
    "Maximum Sensor Rate": 120,
    "Fixed AV Delay": 150,
    "Dynamic AV Delay": "Off",
    "Sensed AV Delay Offset": "Off",
    "Atrial Amplitude": 3.5,
    "Ventricular Amplitude": 3.5,
    "Atrial Pulse Width": 0.4,
    "Ventricular Pulse Width": 0.4,
    "Atrial Sensitivity": 0.75,
    "Ventricular Sensitivity": 2.5,
    "VRP": 320,
    "ARP": 250,
    "PVARP": 250,
    "PVARP Extension": "Off",
    "Hysteresis": "Off",
    "Rate Smoothing": "Off",
    "ATR Duration": 20,
    "ATR Fallback Mode": "Normal", #unknown default
    "ATR Fallback Time": 1,
    "Activity Threshold": "Med",
    "Reaction Time": 30,
    "Response Factor": 8, 
    "Recovery Time": 5
}