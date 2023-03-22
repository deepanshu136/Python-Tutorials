# SETS IN  PYTHON program1
# SET IS ONE OF THE DATATYPE OF PYTHON IT USED  TO STORE THE COLLECTION OF  DATA a SET IS A COLLECTION WHICH IS UNORDERD UNCHENCHABLE AND UNINDEXED
# l=[1,2,3,4,5,5,5,5,6,5,5,7,8]
# s1=list(set(l))
# print(s1)


# a=["a", "s", "d", "a"]
# s2=list(set(a))
# print(s2)
 
# addeing items in  python sets program 2
# people={"Jugal", "Gitanjali", "Aadarsh" ,"Harihar"}
# print(people)
# people.add("Shivam")
# for i in range(1,6):
#     people.add(i)
# print("\nSet afyter adding element:" , end=' ')
# print(people)    

# Union operation in Python sets program 3
# pyhton proram to demonstrate the union of two sets
people={"jugal" , "gitanjali" ,"vaishali" ,"Aadarsh"}
vampires={"Adam","Jack"}
dracula={"nick" , "shadow moon "}
population=people.union(vampires)
print("Union using union() function")
print(population)
