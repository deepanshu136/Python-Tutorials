from email import message
from itertools import count
import pprint
message='It was a bright and a cold day in April, and the clock was striking like thirteen.'
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character] + 1

pprint.pprint(count)    