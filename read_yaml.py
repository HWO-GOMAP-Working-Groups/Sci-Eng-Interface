import os, yaml

def eac1(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/EAC1.yaml', 'r') as f:
        eac1 = yaml.load(f, Loader=yaml.SafeLoader)
   
    return eac1 

def eac2(): 
    
    raise NotImplementedError

def eac3(): 
    
    raise NotImplementedError


def hri(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/HRI.yaml', 'r') as f:
        hri = yaml.load(f, Loader=yaml.SafeLoader)
   
    return hri 

def uvi(): 

    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/UVI.yaml', 'r') as f:
        uvi= yaml.load(f, Loader=yaml.SafeLoader)

    return uvi 

