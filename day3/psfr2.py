"""demo for the file read"""
import pprint

fp = open('passwd.txt', mode='r', encoding='utf-8')

# print(fp.readline())
# print(fp.readline())
# pprint.pprint(fp.readlines())
s = fp.read(10)
print(s)

fp.close()
