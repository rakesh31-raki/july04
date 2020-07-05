# split & join

s = "root:x:0:0:root:/root:/bin/bash"
delimiter = ':'

items = s.split(delimiter)
print(items)
print()

print(s.split(':')[0])  # indexing
print()

print(s.split(':')[1:])
print()

temp = s.split(':')[1:]
print(','.join(temp))
print()

for item in s.split(':')[1:]:  # iterate
    print(item)