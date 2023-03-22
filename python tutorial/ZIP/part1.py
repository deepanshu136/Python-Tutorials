# zip function
user_id=['user1','user2','user3','user4']
name=['Kailash','Abhishek','Deepanshu','Jugal']
a=list(zip(user_id,name))
print(a)
# converting zip into  dictionary
user_id=['user1','user2','user3','user4']
name=['Kailash','Abhishek','Deepanshu','Jugal']
a=dict(zip(user_id,name))
print(a)
# zip is automaticall a tuple here what we are doing is poutting all these tuple inside the single tuple
user_id=['user1','user2','user3','user4']
name=['Kailash','Abhishek','Deepanshu','Jugal']
last_name=['Ram','Kumar','Kumar','Mishra']
a=tuple(zip(user_id,name,last_name))
print(a)

