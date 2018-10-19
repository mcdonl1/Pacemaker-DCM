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
            "AAT": [["LRL", "dropdown",["high", "mid", "low"]], ["URL", "entry"], ["AA", "dropdown", ["Opt 1", "Opt 2"]], ["APW"], ["AS"], ["ARP"], ["PVARP"]],
            "VVT": ["LRL", "URL", "AA", "APW"],
            "AOO": [],
            "AAI": [],
            "VOO": [["LRL", "ranges", ["Choose Range", "30-50 ppm","50-90 ppm" , "90-175 ppm"], "spinbox", [[30,50,5],[50,90,1],[90,175,5]]],["URL", "spinbox", 50, 175, 5],["VA", "dropdown", ["3.75", "Off", "1.25", "2.5", "3.75", "5.0"]],["VPW", "ranges", ["Choose Range", "0.05", "0.1-1.9ms"],"spinbox",[[0.05,0.05,0], [0.1, 1.9, 0.1]]]], #need to add selector for LRL value
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