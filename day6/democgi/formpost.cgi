#!/home/ravijaya/anaconda3/bin/python

import cgi

form = cgi.FieldStorage()
fname = form.getvalue('fname')
lname = form.getvalue('lname')
desg = form.getvalue('desg')
dept = form.getvalue('dept')


print("Content-type: text/html\n")
form = f"""
	<p>frist name : {fname}</p>
	<p>last name : {lname}</p>
	<p>desgination : {desg}</p>
	<p>department: {dept}</p>
"""
print(form)
