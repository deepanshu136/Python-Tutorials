# n=int(input())
# i=1
# while i <= n:
#     j = 1
#     while j<=i:
#         print(j,end='')
#         j=j+1
#     print()
#     i+=1    
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     p=1
#     while j<=i:
#         print(p,end='')
#         j=j+1
#         p=p+1 
#     print()
#     i=i+1 
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end='')
#         j=j+1
#     print()
#     i=i+1
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
        
#         print(j[ : :-1 ,end='')
#         j=j+1
#     print()
#     i=i+1
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i-j+1,end='')
#         j=j+1
#     print()
#     i=i+1
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     start_char=chr(ord('A') +i -1)
#     while j<=i:
        
#         print(chr(start_char+j-1),end='')
#         j=j+1
#     print()
#     i=i+1


# n=int(input())
# i=1
# while i<=n:
#     j=1
#     start_char=(ord('A') + i - 1)
#     while j<=i:
#         print(chr(start_char+j-1),end = '')
#         j=j+1
#     print()
#     i=i+1

# n=int(input())
# i=1
# while i<=n:
#     j=1
#     # start_char=(ord('A'+i-1))
#     while j<=i:
        
#         print(n-i+j,end='')
#         j=j+1
#     print()
#     i=i+1    

# n = int(input())
# i=1
# while i<=n:
#     j=1
#     startchar = chr(ord('A')+n-i)
#     while j<=i:
#         char = chr(ord(startchar)+j-1)
#         print(char, end='')
#         j=j+1
#     print()
#     i=i+1


# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print('1',end="")
#         j=j+1
#     print()
#     i=i+1    
        

# n=int(input())
# i=1

# while i<=n:
#     j=1
#     while j<=(n-i+1):
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1       


# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#      start_char=chr(ord("A")+i-1)
#      print(start_char,end="")
#      j=j+1
#     print()
#     i=i+1 

# n=int(input())
# print(1)
# i=1
# while i<=n-1:
#     j=1
#     while j<=i+1:
#         if (j==1 or j>=i+1):
#             print(i,end='')
#         else:
#             print("0",end="")
#         j=j+1
#     print()
#     i+i+1
# n=int(input())
# print(1)
# i=1
# while i<=n-1:
#     j=1
#     while j<=i:
#        print(i+j-1,end='')
#        j=j+1
#     print()
#     i+=1  
#       
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j <= i:
#         if j == 1 or j == i:
#             print("1", end="")
#     # while j<=i+1:
#         # if(j==1 or j>=i+1):
#         #     print(j,end='')
#         else:
#             print('2',end="")
#         j=j+1
#     print()
#     i=i+1     

# n=int(input())
# i=1
# while i<=n:
#     j=1

#     while j<=n-i+1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1    




# from re import I


# n=int(input())
# i=1
# while i<=n:
#     j=n
#     while j>=i:
#         print(n-i+1,end="")
#         j=j-1
#     print()
#     i=i+1    



# n=int(input())
# i=1
# while i<=n:
#     spaces=1
#     while spaces<=n-i:
#         print(" ",end="")
#         spaces+=1
#     star=1
#     while star<=i:
#         print("*",end="")
#         star+=1
#     print()
#     i=i+1        



# n=int(input())
# i=1
# while i<=n:
#     spaces=1
#     while spaces<=n-i:
#         print(" ",end="")
#         spaces+=1
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1        

# isoceles triangle
# n=int(input())
# i=1
# while i<=n:
#     # spacing
#     spaces =1
#     while spaces <=n-i:
#         print( " ",end='')
#         spaces+=1
#     p=1
#     j=1
#     # increasing 
#     while j<=i:
#         print(p,end="")
#         j=j+1
#         p+=1
#     # decreasing
#     p=i-1
#     while p>=1:
#         print(p,end="")
#         p=p-1
#     print()
#     i+=1        

# n=int(input())
# i=1
# while i<=n:
#     spaces=1
#     while spaces<=n-i:
#         print(" ",end="")
#         spaces+=1

#     j=1
#     # p=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     p=1
#     while p<=i-1:
#         print("*",end="")
#         p=p+1

#     print() 
#     i+=1        
# 


# n=int(input())
# n1=(n+1)//2
# n2=n//2

# row=1
# while row<=n1:
#     spaces=1
#     while spaces<=(n1-row):
#         print(" ",end="")
#         spaces+=1
        
#     star=1
#     while star<=2*row-1:
#         print("*",end="")
#         star+=1
#     print()
#     row+=1
# row=n2
# while row>=1:
#     spaces=1
#     while spaces<=(n2-row)+1:
#         print(" ",end="")
#         spaces+=1
        
#     star2=1
#     while star2<=(2*row)-1:
#         print("*",end="")
#         star2+=1
        
#     print()
#     row-=1    



        
        
        
# def fibonaci_sequence(n):
#     a=1
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(b)
#     else:
#         print(a,b,end="")
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=",")
# n=int(input())
# fibonaci_sequence(n)            
            
        
        
## Read input as specified in the question.
## Print output as specified in the question.
# n=int(input())
# n1=(n+1)//2
# n2=n//2
# row=1
# while row<=n1:
#     spaces=1
#     while spaces <=(row-1):
#         print(" ",end="")
#         spaces+=1
#     star=1
#     while star<= row:
#         print("* ",end="")
#         star+=1
#     print()
#     row+=1 
# row=1     
# while row<=n2:
#     space=1
#     while space<n2-row+1:
#         print(" ",end="")
#         space+=1
#     star2=1
#     while star2 <=n2-row+1:
#         print("* ",end="")
#         star2+=1
#     print()
#     row+=1              
    
    
## Read input as specified in the question.
## Print output as specified in the question.
# lines=int(input()) 
# i=1  
# j=1  
# while i<=lines:  #this loop is used to print lines  
#     j=1  
#     while j<=lines:      #this loop is used to print lines  
#         if i==j:  
#             print("*", end='')  
#         else :  
#             print("0", end='')  
#         j=j+1  
#     j=j-1  
#     print("*", end='', )  
#     while j>=1:  #this loop is used to print lines  
#         if i==j:  
#             print("*", end='' )  
#         else :  
#             print("0", end='')  
#         j=j-1  
#     print("");  
#     i=i+1  

# from operator import truth


# while True:
#     n=int(input())
#     a=int(input())
#     b=int(input())
#     if n==1:
#         c=a+b
#         print(c)
#     elif n==2:
#         c=a-b
#         print(c)
#     elif n==3:
#         c=a*b
#         print(c)
#     elif n==4:
#         c=a//b
#         print(c)
#     elif n==5:
#         c=a%b
#         print(c)
#     elif n==6:
#         break
#     else :
#         print("invalid operation")                    


# n=1
# while n <10:
#     print(n)
#     n+=1
# else:
#     print("it will be printed after the loop is over")



# n=int(input())
# for i in range(1,n+1,1):
#     if i==8:
#         break
#     print(i)
# else:
#     print("it will be printed after the for loop is over")    
 


 
# n=int(input())
# for i in range(1,n+1,1):
#     if i== 12:
#         continue
#     print(i)
# else:
#     print("It will print after the loop is over")   



# n=int(input())
# for i in range(2,n+1,2):
#     if i % 7==0:
#         continue
#     print(i)



# binary pattern
#1111
#000
#11
#0

# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         if i%2 !=0:
#             print("1",end="")
#         else:
#             print("0",end="")    
#         j+=1
#     print()
#     i+=1    




#print the pattern given below
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456
# n=int(input())
# for i in range(1,n+1):
#     if i>1:
#         for space in range(i-1):
#             print(" ",end="")
#         for j in range(i ,n+1):
#             print(j,end="")
#         print()
# rest=n-1
# for i in range (rest,0,-1):
#     for spaces in range(i-1):
#         print(" ",end="")
#     for j in range (i,n+1):
#         print(j,end="")
#     print()                        



# print the diamond pattern fr odd numbers
# n=int(input())
# n1=(n+1)//2
# n2=n//2
# row=1
# while row <=n1:
#     if n%2 != 0:
#         space=1
#         while space<=n1-row:
#             print(" ",end="")
#             space+=1
#         star =1
#         while star<=2*row-1:
#             print("*",end="")
#             star=star+1
#         print()
#         row=row+1
# row=n2
# while row>=1:
#     spaces=1
#     while spaces <= n2-row+1:
#         print(" ",end="")
#         spaces+=1
#     star2=1
#     while star2 <=(2*row)-1:
#         print("*",end="")
#         star2+=1
#     print()
#     row=row-1                        


# FUNCTION ncr factorial formula
# method 1
# n=int(input())
# r=int(input())

# n_fact=1
# for i in range(1,n+1):
#     n_fact=n_fact*i
# r_fact=1
# for i in range(1,r+1):
#     r_fact=r_fact*i
# n_r_fact=1
# for i in range(1,n-r+1):
#     n_r_fact=n_r_fact*i
# ans=n_fact//(r_fact*n_r_fact)
# print(ans)            


# method 2
# by using function

# def fact(n):
#     n_fact=1
#     for i in range(1 , n+1):
#         n_fact=n_fact * i
#     return(n_fact)
# n=int(input())
# r=int(input())
# n_fact=fact(n)
# r_fact=fact(r)
# n_r_fact=fact(n-r)
# ans= n_fact // (r_fact * n_r_fact)
# print(ans)        


#  additon program  using  function
# def add(a,b):
#     return a+b
# total=add(5,4)
# print(total)    


# use of last_char  functuion
# def last_char(name):
#     return name [0:  :]
# print(last_char("abhi"))

# def isPrime(n):
#     for d in range(d , n):
#         if n%d==0:
#             break
#     else:
#       return True
      
#     return False
        

# number = int(input())
# temp = number
# add_sum = 0
# while temp!=0:
#     k = temp%10
#     add_sum +=k*k*k
#     temp = temp//10
# if add_sum==number:
#     print('true')
# else:
#     print('false')        
# lines=int(input()) 
# i=1  
# while(i<=lines):# this loop is used to print lines  
#     j=lines  
#     while (j>=1):# this loop is used to print numbers in a line  
#         if j!=i:  
#             print(j, end='', flush=True)  
#         else:  
#             print('*', end='', flush=True)  
#         j=j-1  
#     print("")  
#     i=i+1;  




