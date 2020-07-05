param = ['lang', 'author', 'version', 'release']
values = ('perl', 'larry', 5.5, 'parrot')


print(zip(param, values))

for item in zip(param, values):
    print(item)
print()

print(dict(zip(param, values)))
