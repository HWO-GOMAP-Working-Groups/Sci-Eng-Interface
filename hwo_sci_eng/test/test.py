from hwo_sci_eng.utils import read_json, read_yaml 

eac1 = read_yaml.eac1()
print() 
print() 
print() 
print('EAC1 YAML') 
print(eac1) 


eac2 = read_yaml.eac2()
print() 
print() 
print() 
print('EAC2 YAML') 
print(eac2) 



eac3 = read_yaml.eac3()
print() 
print() 
print() 
print('EAC3 YAML') 
print(eac3) 


#------------ 


eac2 = read_json.eac2()
print() 
print('EAC2 JSON') 
print(eac2) 

eac3 = read_json.eac3()
print() 
print('EAC3 JSON') 
print(eac3) 

