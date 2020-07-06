import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match

m = re.search(pattern, s, re.IGNORECASE)

if m:
    print(m)
    print('match string :', m.group())
    print(m.start())
    print(m.end())
else:
    print('failed to match')
