import os, yaml

paths = {
    "eac1": "/obs_config/Tel/EAC1.yaml",
    "eac2": "/obs_config/Tel/EAC2_draft.yaml",
    "eac3": "/obs_config/Tel/EAC2_draft.yaml",
    "hri": "/obs_config/HRI/HRI.yaml",
    "uvi": "/obs_config/UVI/UVI.yaml",
    "ci": "/obs_config/CI/CI.yaml"
}

def read_eac(component):
    """
    A generic component reader
    """
    with open(os.getenv('SCI_ENG_DIR') + paths[component.lower()], 'r') as f:
        comp_yaml = yaml.load(f, Loader=yaml.SafeLoader)
   
    return comp_yaml

def eac1():
    return read_eac("eac1")

def eac2():
    return read_eac("eac2")

def eac3():
    return read_eac("eac3")

def hri():
    return read_eac("hri")

def uvi():
    return read_eac("uvi")

def ci():
    return read_eac("ci")
