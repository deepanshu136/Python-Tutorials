#  list comprehension with if else program1
number=[i for i in range(11) if i %2!=0]
print(number,'is odd')
number=[i for i in range(11) if i %2==0]
print(number,'is even')

# program 2
nums =[1,2,3,4,5,6,7,8,9,10]
new_list=[i*2 if (i%2==0) else -i for i in nums]
print(new_list)

