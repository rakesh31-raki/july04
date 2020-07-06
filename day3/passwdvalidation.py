"""
#@_!%$
0-9
a-z
A-Z
8, 12
"""
import re
import getpass

password = getpass.getpass()
if 8 <= len(password) <= 12:
    if re.search('[#@_!%$]', password) and re.search('[0-9]', password) and re.search('[a-z]', password) and  \
            re.search('[A-Z]', password):
        print(f'{password} valid password'


# email, ipv4 address (a.b.c.d)

