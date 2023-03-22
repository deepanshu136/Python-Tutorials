# use of sort in list
# eadible=['grapes','cake','apple','toofee','cashew']
# eadible.sort()
# print(eadible)

# we cannot use sort function in tuple so here we use sorted( ) function and tuples are imutable so it wil give us list in sorted order so convert it into tuple using tuple
# eadible=['grapes','cake','apple','toofee','cashew']
# print(tuple(sorted(eadible)))

# now sort in sets and we know that sort does't have any order lets see what happen?
# eadible={'grapes','cake','apple','toofee','cashew'}
# print(sorted(eadible))


# practice 
# guitars=[
#     {'model':'yamaha f310','price':8400},
#     {'model':'faith neptune','price':50000 },
#     {'model':'gibson','price':30000},
#     {'model':'taylor 814ce','price':450000}
# ]
# print(sorted(guitars,key=lambda item: item.get('price')))

# p2
# user=int(input(""))
# add=0
# i=1
# while i<=user:
#     add+=i
#     i=i+1
# print(add)    
#  or
# def fun(n):
#     add=0
#     for i in range(1,n+1):
#         add=add+i
#     return add
# print(fun(22))  