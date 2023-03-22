# program 1
# import re
# phoneNumRegx=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
# no=phoneNumRegx.search("my number is : 412-412-2323")
# no.group()
# print(no.group(1))
# print(no.group(2))
# print(no.group(0))
# print(no.group())

# program2
import re
phoneNumRegx=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
no=phoneNumRegx.search('415-555-3434')
no.group()
areaCode, mainNumber=no.group(1) , no.group(2,3) 
print(areaCode)
print(mainNumber)

