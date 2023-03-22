# keys(),values(),items()Methods
# spam={'color':'blue','age':'54'}
# for v in spam.values():
#     print(v)


#now use of keys() with this we can itereate over keys or over keya and both values
# spam={'color':'red','age':'34'}
# for i in spam.keys():
#     print(i) 


# now use of items
# spam={'color':'red','age':'34'}
# for i in spam.items():
#     print(i) 


# spam={'color':'red','age':'34'}
# spam.keys()
# dict_keys=(['colors','age'])
# print(list(spam.keys()))


# NOW CHECK WETHER A KEY OR VALUES EXISTS IN DICTIONARY
# spam={'color':'red','age':'34'}
# print('color' in spam.keys())
# print('grey' in spam.items())


# GET METHODS 
# picnicItems={'apples':'6','cups':'3'}
# print('Iam bringing '+str(picnicItems.get('cups',0))+' cups')
# print('Iam bringing ' + str(picnicItems.get('eggs',0))+ ' eggs')

# SET DEFAULT METHODS
spam={'name':'jugL','age':'22'}
spam.setdefault('color','black')
print(spam)
spam.setdefault('color','white') #as we can see color is not updated here because already has a keys name color whose values is blsck
print(spam)