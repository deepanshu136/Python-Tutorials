# Using list comprehension to iterate through loop program1
# list=[i for i in[1,2,3,4,5]]
# print(list)

# Even list using list compression program 2
# list=[i for i in range(int(input(""))) if i%2 == 0]
# print(list)

# Matrix using list compression program 3
# matrix = [[j for j in range(3)] for i in range(3)]
   
# print(matrix) 

# LIST COMPARRISION VS FOR LOOP 
# program 4 common approach
List=[]
for character in 'Geeks for Geeks':
    List.append(character)
print(List)    

# now doing it with the help of for loop
List=[character for character in ' Geeks for geeksHH']
print(List)