# shallow copy vs deep copy

items = [2, 3, 4]
backup = items.copy()

items.pop()
print(items)
print(backup)