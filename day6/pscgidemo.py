import cgi

form = cgi.FieldStorage()
fname = form.getvalue('fname')
lname = form.getvalue('lname')
desg = form.getvalue('desg')
dept = form.getvalue('dept')