# numbers=[1,2,3,4]
# def square(s):
#     return s**2
# squares=list(map(square, numbers))
# print(squares) 

# numbers=[1,2,3,4]
# new=[]
# for num in numbers:
#      new.append(num**2)
# print(new)     

# question you have a list of names=["asd","ad","asdd"] you have to count the length of each string
names=["asd","ad","asdd"] 
length=map(len,names)
for i in length:
    print(i)