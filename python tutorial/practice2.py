# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum (pair)/len(pair))
#     return average
# print(average_finder([1,2,3.99],[3,5,6,76],[34,456,67,56])) 

# program 2
# number=[2,4,8,5,10]
# evens=[]
# for num in number:
#     if (num % 2 == 0):
#         evens.append(True)
#         evens.append(num)
# print(evens)
# now doing above prgram with  list comprehension
# print(all([num%2==0 for num in number]))

# program 3 any()
# bsaiscally aby function will return true if we have any one true in our list,.. otherwise it will automatically return false
# number2=[2,4,5,8]
# print(any([i%2 !=0 for i in number2]))


# program 4
# def my_sum(*args):
#     if all([(type(arg)==int or type(arg)==float) for arg in args]):
#      total=0
#      for num in args:
#         total+=num
#      return total  
#     else:
#        return("wrong input")
# print(my_sum(2,4,5))  

# program 4 min and max
# number=[1,2,3,6,9]
# print(min(number))
# print(max(number))

names=['Deepanshu','Jugal','Gitanjali']
print(max(names, key =  lambda item : len(item))) 

students={
    'Deepanshu':{'score':90 , 'age': 21},
    'Jugal':{'score':80 , 'age': 26},
    'Gitanjali':{'score':98 , 'age': 22},
}
print(max(students, key= lambda item1 : students[item1]['score']))

students2=[
    {'name':'Deepanshu', 'score':90, 'age': 24},
    {'name':'deepak', 'score':97, 'age': 28},
    {'name':'Geetu', 'score':99, 'age': 20},
]

print(max(students2,key=lambda item:item.get('name'))['name'])
