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
paramArrays = {   
            "AAT": [["LRL", "dropdown",["high", "mid", "low"]], ["URL", "entry"], ["AA", "dropdown", ["Opt 1"]], ["APW"], ["AS"], ["ARP"], ["PVARP"]],
            "VVT": ["LRL", "URL", "AA", "APW"],
            "AOO": [],
            "AAI": [],
            "VOO": [],
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
    
}