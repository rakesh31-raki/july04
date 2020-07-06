"""random file processing  -> binary """

""" file-mode        text , binary (images, pdf, exe, mp3, mp4)
    read                r    rb
    write               w    wb   
    append              a    ab          
"""
fp = open('passwd.txt', 'rb')

print(fp.read(10))
print(fp.tell())

# position the file pointer at 50th  bytes
fp.seek(40, 1)  # whence as 1, form the current position

print(fp.read(10))
print(fp.tell())

# to read the last 10 bytes
fp.seek(-10, 2)   # whence is 2, it denotes from end of file
print(fp.tell())
print(fp.read())

fp.close()

# bytes string
# pyexcel