tiny = [2.2, 3, 4, 5, 0.98]

print(tiny + tiny)
print()
print(tiny * 3)
print()

duplicates = [2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98, 2.2, 3, 4, 5, 0.98]
print(set(duplicates))  # unordered collections
unique = list(set(duplicates))
print(unique)