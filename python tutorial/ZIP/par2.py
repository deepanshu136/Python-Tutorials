# l=[(1,2),(3,4),(5,6),(7,8)]
# l1,l2=(list(zip(*l)))
# print(list(l1))
# print(list(l2))

# program 2
l1=[1,3,5,7]
l2=[2,4,6,8]
l3=[]
for pair in zip(l1,l2):
    l3.append(max(pair))

print(l3)    
