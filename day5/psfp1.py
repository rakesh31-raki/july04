"""functional programming"""

items = [1, 3, 2, 4, 5, 6]

m = map(hex, items)
print(m)
print()

for item in m:
    print(item)

print()

m = map(ord, 'peter pan')
print(list(m))

# print(hex)
# print()
# print(hex(15))
