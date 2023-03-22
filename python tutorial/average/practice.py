# student_scores=input("Input a list os students scores").split()
# for n in range(0 , len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)
# heighest_score=0
# for score in student_scores:
#     if score>heighest_score:
#        heighest_score = score
# print(f"the heighest inty he class is:{heighest_score}")        
    


    # sum of n numbaer in python
# total=0
# for i in range(1,101):
#     total+=i
# print(total)   

# sum of all even number
# total=0
# for i in range(1,101):
#     if(i%2==0):
#         total+=i
# print(total)       

for i in range(1,101):
    if(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0 and i%4==0 ):
        print("fizzbuzz")  
    else:
     print(i)            




