"""Context manager  its grantees on closing the file """

with open('passwd.txt', mode='rb') as fp:

    for temp in fp:
        print(temp, end='')

