#chapter2
#string concatination
a=" deepanshu "
b=" kumar "
print(a+b)#or you can make a new varible in which you store the value by concaniating two string and then print tha variable value
#you cannot add the number with string
#only string can be added together
# now to add the number with string you have to chane the int to string then concanitae that string for example given below by using str or ""
name=("Deepanshu ")
sirname=("Kumar")
c=1
print(" Your first name is "+ name + " and last name is " + sirname + str(c))
#to print string multiple time   we can use * this example given below
d=("Adarsh\n")
print(d*100)
#to take user from input we use input function
e=input(" Enter your name")
print(" hello " +e)#input function will always take the input from user in string
age=input("What is your age")
print("Your age is " + age)
#use of int()function
first_number=int(input("Enter first number"))
second_number=int(input("Enter second number"))
total=first_number+second_number
print("your total is " + str(total))
#str
#4-->"4"
#int
#4--> 4
#float
#6-->6.0
#using  above thee function in proogram given below byy adding
number=(6)
number1=float("43")
number2=int("33")
print(number+number1+number2)#final answer will be in float
#taking more then one variable in same line
name2,age2=("jaguar",23)
print("HELLO " + name2 +" Your age is " + str(age))
#taking more than one input in same line by using.split()
hobby , sport=input("What is your hobby and sport").split()
print(hobby)
print(sport)
#string formatting
name4=("hj")
age4=23
print(f"hello {name4} your age is {age4}" )
##Extercise
#ask user to input 3 numbers and you have to print average of three number using string formatting
j=int(input("first value\n"))
k=int(input("second number\n"))
l=int(input("third number\n"))
sum=j+k+l
average=sum/3
print(str(average))
#string indexing
#according to string indexing by this we can see that at which position which character is stored twe can check the position from starting and end
climate=("AUTUMN")
print(climate[0])
print(climate[1])
print(climate[2])
print(climate[3])
print(climate[4])
print(climate[5])
sound=("horn")

print(sound[-1])
print(sound[-2])
print(sound[-3])
print(sound[-4])
#print(sound[-5])
##string slicing/slecting sub sequence
subject=("ENGLISH")
print(subject[0:3])
print(subject[2:7])
#if starting the indexing from last
pen=("MONTEX")
print(pen[-1:-3])
print(pen[ 1:])
print(pen[ : 4])
##step argument
snake=("ANACONDA")
print(snake[0:8:1])
print("DEEPANSHU"[0:8:3])
print("DEEPANSHU"[ : 5 :2])
print("DEEPANSHU"[ 1: :3])
print("harshit"[ : : -1])#reversing the string
print("harshit"[ : : -2])#reversing the string with step argument
print("harshit"[2 : : -2])
##Exercise
#ask user name and print back user na,e in reverse order
user=input(" Enter your name ")
print(f"your reversing name is {user[-1 : :-1]}" )
##STRING METHOD
#types of string fundtion
#len()it is used to count the number of character in our string(it also count the spaces)
k=len("MAHABARATH")
print(k)
j=len("ARJ   UN")
print(j)
#lower()method
k=("BHEEM")
print(k.lower())#change all the charscter in lower case letter
#upper()method
l=("tom holland")
print(l.upper())
#title method
m=("deepanshu")
print(m.title())#it converst the first charcter in uppercase and the rest will be in lower case
n=("rAHAT FATAH ALI KHAN")
print(n.title())
#count()method
o=("terrenterrino")#it count the ceratin character is how many time used in our string
print(o.count("r"))
###exercise
#take two comma seperated input from user
#1 user's name
#2a single character
#output should be
# users name length
#count the character that user inputed(bonous:count case insensitve count)
namee1,char=input("your names are").split(",")
print(f"length of your name is: {len(namee1)}")
print(f"charcter count: {name.lower().count(char.lower())} ")
#print(len(namee1))
##STRIP METHOD to remove the space from left side and right side
#for left use l.strip(),for right use r.strip() and to remove both the space use strip()
planet=("    Mercury    ")
print(planet )
print(planet.lstrip())
print(planet.rstrip())
print(planet.strip())
print(planet.replace(" ", ""))
##find and replace method
#replace () it is used to replace anything inside the string
string=("She is a beautiful  dancer")
print(string.replace(" ","_"))
print(string.replace("beautiful","versetile"))
#find method()used to find the position of any world or chae
string1=("she is beautifulS and she is good dancer")
print(string.find("beautiful"))
pos1=string1.find("is")
pos2=string1.find("is" , pos1+1)
print(pos2)
print(string1[0])
print("\U0001F609\n"*200)
###CENTER METHOD
sam=("seasonal")
print(sam.center( 10 ,"*"))
soo=input("enter your name")
print(soo.center(len(soo)+8,"*"))
jo=input("enter your name")
print(jo.title().center(len(jo)+10,"$"))
kile=input("Enter your name")
print(kile.upper().center(len(kile)+6,"@"))
james=input("hey which month is this ")
print(james.title().center(len(james)+10,"#"))
##string are immutable
##in  python syring is immutable means ones defined cannot be changed
stringo=("football")
print(stringo.replace("f","F"))
jack=("Germany")
string.replace("e","E")
print(string)
new_jack=(string.replace("e","E"))
print(new_jack)
##ASSIGNMENT OPERATORS
z=("deepanshu")
z+="kumar"
print(z)
old=21
old+=1
print(old)











