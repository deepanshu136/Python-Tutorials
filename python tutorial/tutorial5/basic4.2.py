##EXERCISE
#ask a user for name
#Example - harshit vashistha
#print count of each world
name=input("please enter your name")
temp_var=""
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var+= name[i]
    print(f"{name[i]} : {name.count(name[i])}" )
    i+=1
