import os, yaml

paths = {
    "eac1": "/obs_config/Tel/EAC1.yaml",
    "eac2": "/obs_config/Tel/EAC2_draft.yaml",
    "eac3": "/obs_config/Tel/EAC2_draft.yaml",
    "hri": "/obs_config/HRI/HRI.yaml",
    "uvi": "/obs_config/UVI/UVI.yaml",
    "ci": "/obs_config/CI/CI.yaml"
}

def read(component):
    """
    A generic component reader
    """
    with open(os.getenv('SCI_ENG_DIR') + paths[component.lower()], 'r') as f:
        comp_yaml = yaml.load(f, Loader=yaml.SafeLoader)
   
    return comp_yaml
