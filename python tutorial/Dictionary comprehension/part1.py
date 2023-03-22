square={num:num**2 for num in range(11)}
print(square)

# counting the number of character in the string 
string="deepanshu"
word_count={char:string.count(char) for char in string}
print(word_count)

# merging dictionaries 
dict1={'w':1 ,'x':2}
dict2={'x':2 ,'y':2, 'z':2}
dict3={k:v for d in [dict1,dict2] for k ,v in d.items()}
print(dict3)
