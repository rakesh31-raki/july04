"""demo for the file write"""

print(range(1, 11))
print()

fw = open('output.txt', 'w')

for item in range(1, 11):
    fw.write(f'the sample message : {item}\n')

fw.close()
