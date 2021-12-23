
with open('mal.txt','r') as b:
    a = b.read()


c = a.split('*')



array = "["
for elem in c:
    array+= f""" "{elem.strip()} " ,"""
array+= ']'

print(array)

with open('output.json','w') as f:
    f.write(array)