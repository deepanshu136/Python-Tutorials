# enumtrate function in python
# use for tracking the position in list and tuple with the help of  for loop
name=["Abhishek","deepanshu","kailash"]
pos=0
for i in name:
    print(f'{pos} -----> {i}')
    pos+=1
# program 2
name1=["deepanshu" , "ad","mummy"]
pos1=0
for pos,name in enumerate(name1):
    print(f"{pos1} -----> {name}")
    pos+=1

#program 3
def find_pos(l, target):
    for pos, name1 in enumerate(l):
         if name1== target:
             return pos

    return -1

print(find_pos(name1,"mummy")) 