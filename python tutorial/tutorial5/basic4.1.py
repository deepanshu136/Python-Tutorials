##EXERCISE2 in while loop
#ask a user to  input a number contaning more then one digit
#example=1234
#calculate=1+2+3+4
number=input("enter the number")
total1=0
i3=0
while i3<len(number):
    total1+=int(number[i3])
    i3=i3+1
print(total1)

name=input("enter your name")
temp=""
i=0
while i< len(name):
    if name[i] not in temp:

        temp= temp + name[i]
        print( f"{name[i]}: {name.count(name[i])}")
        i=i+1