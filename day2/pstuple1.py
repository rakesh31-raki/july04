items = (2.2, 1, 2, 3, 'tim', 'pat', 'tom')
print(items)
print(len(items))
print(type(items))
print()

# items[-3] = 'timmy'  # immutable

print(items[-3])  # indexing
print()

print(items[-3:])  # slicing
print()

for item in items[-3:]:
    print(item)