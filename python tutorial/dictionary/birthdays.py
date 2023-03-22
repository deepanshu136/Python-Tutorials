from unicodedata import name


birthdays={'bhai':'20 march',
'papa':'30oct',
'gunnu':'10 july',
'shantanu':'10 janurary',
'gitanjali': '21 june',
'jugal':'29 november',
'harihar':'12 janurary',
'Aadarsh':'15march'}
while True:
    print('Enter a name : (blank to quit)')
    name=input()
    if name =='':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthdays of ' + name)
    else:
        print('I do not have birthdays information of' + name)
        print('What is their birthdays?')
        bday=input()
        birthdays[name]=bday
        print('Database is updated')     