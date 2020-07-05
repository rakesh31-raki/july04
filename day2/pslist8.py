duplicates = [2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98]
s = sorted(duplicates)
print(duplicates)
print(s)
print()

duplicates = [2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98]
sorted( duplicates, reverse=True)  # inplace edit
print(duplicates)
print(s)
print()

duplicates = [2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98]
# duplicates.reverse()
r = reversed('perl')
print(duplicates)
print(r)

for item in r:
    print(item)