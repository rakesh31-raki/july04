"""demo for the file read"""

fp = open('passwd.txt', mode='r', encoding='utf-8')

# print(fp)
# print(type(fp))
for temp in fp:
    print(temp, end='')

fp.close()