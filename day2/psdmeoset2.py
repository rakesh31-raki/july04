# set aka hashed list = hash + list, unordered collection
# mutable
items = {2, 1, 3, 'pam', .90, 'allen'}

print(items)
print(len(items))
print()

items.add(1.2)
items.add('brillio')
items.add('bangalore')
print(items)
print()

items.remove('pam')
items.remove(3)
print(items)
print()

# iterate
for item in items:
    print(item)
