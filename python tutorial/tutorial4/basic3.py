##CHAPTER3
#if conditin :it checks weather the given conditio is true or not if true then the programmm will execute
user=input("Enter your name:")
age=int(input("enter your age"))
if age==12:
    print("hello" ,user.title())
    print("you are eligible")
##pass statement
x=19
if x>19:
    pass
##if else statement
name=input("HEY! What's your name")
old=int(input("How old are you "))
if old>=19:
    print("Welcome",name.title())
    print("You are eligible for all the game")
else:
    print("Sorry,you are not eligible to play all the game") 
##
a=int(input("enter the value"))
b=int(input("enterthe value"))
c=a+b
print(str(c))
if c==59:
    print("your addition is not correct")
else:
    print("you addition is currect")    

 ##exercise(guessing number game)
winning_number=("34")
user1=int(input("guess a number"))
print(str(user1))
if user1==34:
    print("YEEEEy you won")
else:
    if user1<34:
        print("too low")
    if user1>34:
        print("tooo high")    
###AND OR OPERATOR
name2=("joe biden")
age=23
if name2=="joe biden" and age==23:
    print("both condition are true")
else:
    print("condition false")
namee=("jaspreet")
age=13
if namee=="jaspreet" and age==12:
 print("your coondition is true") 
else:
    print("your conditon is not true")
 ##or operator
actor=("Chris Evans")
movie=("captain america")
if actor=="chris evans" or movie=="captain america":
    print("you are correct")
else:
    print("you are wrong")

actress=("Angeolina jollie")
movie1=("Eternals")
if actress==("Angeolina jollie") or movie1==("GI JOE"):
    print("correct guess")
else:
    print("wrong guess")    

my_name=("deepanshu")
my_age=(21)
if my_name==("Adarsh") or my_age==34:
    print("you are phenominal")
else:
    print("you are dumb")       

##Exercise
# exercise :watch cooco
# asks users name and age
# if users name starts with(a or A) and age is above 10 then
# print you can watch cooc movie
# else print "sorry you cant watch the movie"
#
# SOLUTION
#
movie_name=("cooco")
user_name=input("enter your name")
user_age=int(input("enter your age"))
print("your name is",user_name)
print("your entered age is:",str(user_age))
if user_name[0]==("A") or user_name[0]==("a") or user_age>10:
    print("you can watch movie",movie_name)
else:
    print("you cannot watch",user_name)  

###if ,elif,else statement
# used to check multiple condition at same time
###TICKET PRICE MACHINE
NAME=input("Your name is:")
age =input("your age is:")
age=int(age)
print(NAME)
if age==0:
    print("You cant't watch.")
elif 0<age<=3:
    print("Ticket price : FREE")
    print("\U0001F603"," Yeeey You are lucky" )
elif 3<age<=10:
    print("Ticket price : 150 ")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")    

 ###USE OF in KEYWORD with if
users_name=input("enter user name : ")
print(users_name)
if ("d") in (users_name) or ("k") in (users_name):
    print("the given characternis present:")
else:
    print("the given character is not present:")  

 ##check empty or not
name5=("HArshit")     
if name5:
    print("String is not empty.")
else:
    print("String is empty.")

#1
name6=input("enter your name.")
if name6:
    print(f"your name is{name6}")          
else:
    print("you didn't enter anything.")  
            




        



