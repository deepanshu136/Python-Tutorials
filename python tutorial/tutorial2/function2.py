# def last_char(name):
#     return name[-1]
# print(last_char("abhi"))      

# def odd_even(num):
#     if num%2 ==0 :
#         return("even")
#     else:
#      return("odd")
# print(odd_even(8))

# def greater_number(a,b):
#      if a> b:
#          return a
#      else:
#          return b

# def new_greatest(a,b,c):
#     bigger= greater_number(a,b)
#     return greater_number(bigger,c)
# print(new_greatest(1,34,67))    


   
# def hello_world():
#     print("deepanshu kumar")
# hello_world()

    
# def sum():
#     a=10
#     b=20
#     c=a+b
#     return c
# print(sum())        
    




# def sum():
#     c=a+b
#     return c
# a=int(input())
# b=int(input())
# print(sum())    


# li=[1,2,3,4,5,2.34]
# v=type(li)
# print(v)
# print(li)

## Read input as specified in the question.
## Print output as specified in the question.
# n=int(input())
# i=1
# j=1
# while i<=n:
#     j=1
#     while j<=n:
#         if(i==j):
#             print("*",end="")
#         else:
#             print("0",end="")
#         j=j+1
#     j=j-1
#     print("*",end="")
#     while j>=1:
#         if i==j:
#             print("*",end="")
#         else:
#             print("0",end="")
#         j=j-1
#         print()
#         i=i+1
 #
# catNames=[]
# while True:
#     print("Enter the name of your cat"+ str(len(catNames)+1)+'(Or enter nothing to stop):')
#     name=input(" ")
#     if name =="":
#         break
#     catNames=catNames+[name]
#     print(" the cat names  are:")
# for name in catNames:
#     print(" " + name)

i=0
for i in range(4):
    print(i)