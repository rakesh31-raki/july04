import re

pattern = '^r'

matched_lines = filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd'))

for line in matched_lines:
    print(line, end='')