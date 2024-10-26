import os, yaml

def eac1(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/Tel/EAC1.yaml', 'r') as f:
        eac1 = yaml.load(f, Loader=yaml.SafeLoader)
   
    return eac1 

def eac2(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/Tel/EAC2_draft.yaml', 'r') as f:
        eac2 = yaml.load(f, Loader=yaml.SafeLoader)

    return eac2 

def eac3(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/Tel/EAC3_draft.yaml', 'r') as f:
        eac3 = yaml.load(f, Loader=yaml.SafeLoader)

    return eac3 

def hri(): 
    
    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/HRI/HRI.yaml', 'r') as f:
        hri = yaml.load(f, Loader=yaml.SafeLoader)
   
    return hri 

def uvi(): 

    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/UVI/UVI.yaml', 'r') as f:
        uvi= yaml.load(f, Loader=yaml.SafeLoader)

    return uvi 

def ci(): 

    with open(os.getenv('SCI_ENG_DIR') + '/obs_config/CI/CI.yaml', 'r') as f:
        ci = yaml.load(f, Loader=yaml.SafeLoader)

    return ci 

