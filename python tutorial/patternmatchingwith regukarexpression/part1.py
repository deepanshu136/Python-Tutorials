import re   
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
no=phoneNumRegex.search("My number is 455-555-9898")
print('phone no.founmd:' +no.group())


# in regular expression  the following character have special meaning . ^ $ * + ? { } [ ] \ | ( )
#  if we want  detect these character as a part of your text pattern then we need to escape them with \(backslash): \. \^ \* ---------

