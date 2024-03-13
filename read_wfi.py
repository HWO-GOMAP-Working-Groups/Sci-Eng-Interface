import json

# Opening JSON file
with open('WFI.json', 'r') as openfile:

# Reading from json file
wfi = json.load(openfile)
   
print(wfi) 
print(type(wfi))
