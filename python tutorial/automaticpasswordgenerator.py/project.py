# password generator
import random
letters=[ ' a ' , ' b ' , ' c ' , ' d ' , ' e ' , ' f ' ,'F ' , ' g ' , ' h ' , ' i ' , ' J ',' j ' ,'W ' , ' l ' , ' m ' , ' n ' , ' o ' , ' p ' , ' q ' , ' r ' , ' s ' , ' t ' , ' u ' , ' v ', ' D ' , ' E ' , ' F ' , ' G ' , ' H ' , ' I ' , ' J ' , ' K ' ,' T ' , ' U ' , ' V ' , ' W ' , ' X ' ,' y ' , ' z ' , ' A ' , ' B ' , ' C ' ,' Q ' , ' R ' , ' S ' , ' L ' , ' M ' , ' N ' , ' 0 ' , ' P ' ,
' Y ' , ' Z ']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['1','@','#','$','%','^','&','*','(',')','~','+','/','?']
print("Welcome to the password generator!")
nr_letter=int(input("How many letter would you like to suggest?\n"))
nr_symbol=int(input("how many symbol would you like to take?\n"))
nr_number=int(input("how many number would you like to take?\n"))
password=[]
for char in range(1,nr_letter+1):
    password.append(random.choice(letters))
for char in range(1,nr_symbol+1):
    password+=random.choice(symbols)
for char in range(1,nr_number):
    password+=random.choice(numbers)

random.shuffle(password)
  
passw=""
for char in password:
    passw+=char
print(f"your password is:{passw}")    


