import os.path as path
import os

fp = open('path.txt')

for line in fp:
    line = line.rstrip()  # trailing \n char from the line
    print(path.basename(line))
    print(path.dirname(line))
    print()

fp.seek(0, 0)   # at begin of the file , whence is 0
print(fp.readlines())
fp.close()