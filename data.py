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

# modesAsNumber = {
#             "Select a Mode",
#             "AAT": 0 ,
#             "VVT": 1,
#             "AOO": 2,
#             "AAI": 3,
#             "VOO": 4,
#             "VVI": 5,
#             "VDD": 6,
#             "DOO": 7,
#             "DDI": 8,
#             "DDD": 9,
#             "AOOR": 10,
#             "AAIR": 11,
#             "VOOR": 12,
#             "VVIR": 13,
#             "VDDR": 14,
#             "DOOR": 15,
#             "DDIR": 16,
#             "DDDR": 17
# }
#Each mode's parameters and their method of input
#for dropdown menu, need to specify list of options

#Entry - [Param]
#Dropdown - [Param, "dropdown", [options]]
#Spinbox - [Param, "spinbox", from, to, increment]

paramArrays = {   
            "AAT": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]], ["Upper Rate Limit", "spinbox", 50, 175, 5], ["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "VVT": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]], ["Upper Rate Limit", "spinbox", 50, 175, 5], ["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "AOO": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "AAI": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "VOO": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]], #need to add selector for Lower Rate Limit value
            "VVI": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "VDD": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "DOO": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "DDI": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "DDD": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]],
            "AOOR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "AAIR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]], ["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "VOOR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "VVIR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "VDDR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "DOOR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0.01], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "DDIR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
            "DDDR": [["Lower Rate Limit", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["Upper Rate Limit", "spinbox", 50, 175, 5],["Ventricular Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Atrial Amplitude", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["Ventricular Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Atrial Pulse Width", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]],["Activity Threshold","dropdown",["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]]],
}
# stores current values of each parameter - modified by parameter edit screen each time a parameter is changed
currentValues = {
    "Mode": ["DDD",""],
    "Lower Rate Limit": ["60","ppm"],
    "Upper Rate Limit": ["120","ppm"],
    "Maximum Sensor Rate": ["120","ppm"],
    "Fixed AV Delay": ["150","ms"],
    "Dynamic AV Delay": ["Off",""],
    "Sensed AV Delay Offset": ["Off",""],
    "Atrial Amplitude": ["3.5","V"],
    "Ventricular Amplitude": ["3.5","V"],
    "Atrial Pulse Width": ["0.4","ms"],
    "Ventricular Pulse Width": ["0.4","ms"],
    "Atrial Sensitivity": ["0.75","mV"],
    "Ventricular Sensitivity": ["2.5","mV"],
    "VRP": ["320","ms"],
    "ARP": ["250","ms"],
    "PVARP": ["250","ms"],
    "PVARP Extension": ["Off",""],
    "Hysteresis": ["Off",""],
    "Rate Smoothing": ["Off",""],
    "ATR Duration": ["20","cc"],
    "ATR Fallback Mode": ["Normal",""], #unknown default
    "ATR Fallback Time": ["1","min"],
    "Activity Threshold": ["Med",""],
    "Reaction Time": ["30","sec"],
    "Response Factor": ["8",""], 
    "Recovery Time": ["5","min"]
}

# #stores current values of each parameter - modified by parameter edit screen each time a parameter is changed
# currentValues = {
#     "Mode": ["DDD",""],
#     "Lower Rate Limit": ["60","ppm"],
#     "Upper Rate Limit": ["120","ppm"],
#     "Atrial Amplitude": ["3.5","V"],
#     "Ventricular Amplitude": ["3.5","V"],
#     "Atrial Pulse Width": ["0.4","ms"],
#     "Ventricular Pulse Width": ["0.4","ms"],
#     "Activity Threshold": ["Med",""]
# }

currentUser = ""