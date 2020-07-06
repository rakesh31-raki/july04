import re


def grep_me(pattern, filename):
    with open(filename) as fp:
        for line in fp:
            if re.search(pattern, line, re.I):
                print(line, end='')


regexp = '^r'
filename = 'passwd.txt'

grep_me(regexp, filename)
