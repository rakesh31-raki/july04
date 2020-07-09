#!/home/ravijaya/anaconda3/bin/python
from time import ctime
from sys import version

print("Content-type: text/html\n")

content = f"""
<html>
  <head>
	<title>a sample cgi application : {ctime()}</title>
  </hread>
  <body>
	<h2>{ctime()}</h2>
    <pre>{version}</pre>
  </body>
</html>
"""

print(content)
