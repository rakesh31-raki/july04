#!/home/ravijaya/anaconda3/bin/python
from os import environ


print("Content-type: text/html\n")
rows = ''
r = 1

for name, value in environ.items():
	color = '#dbdbdb' if r%2 else ''
	rows += f'<tr bgcolor="{color}"><td>{name}</td><td>{value}</td></tr>'
	r += 1	

content = f"""
<html>
  <head>
	<title>server env</title>
  </hread>
  <body>
	<table align="center" cellspacing="5" cellpadding="5">
	<tr><th>Name</th><th>Value</th></tr>
	{rows}
	</table>
  </body>
</html>
"""

print(content)
