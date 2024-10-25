import os, json

def eac1(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/json/Telescope-EAC1.json', 'r') as openfile:
        eac1 = json.load(openfile)
   
    return eac1 

def eac2(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/json/Telescope-EAC2.json', 'r') as openfile:
        eac2 = json.load(openfile)
   
    return eac2 

def eac3(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/json/Telescope-EAC3.json', 'r') as openfile:
        eac3 = json.load(openfile)
   
    return eac3 

def wfi(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/json/WFI.json', 'r') as openfile:
        wfi = json.load(openfile)
   
    return wfi 

def uvs(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/json/UVS.json', 'r') as openfile:
        uvs = json.load(openfile)
   
    return uvs 

