#!/home/ravijaya/anaconda3/bin/python


print("Content-type: text/html\n")
form = """
<form action="formpost.cgi" method="post">
	<p>frist name : <input type="text" name="fname" /></p>
	<p>last name : <input type="text" name="lname" /></p>
	<p>desgination : <input type="text" name="desg" /></p>
	<p>department: <input type="text" name="dept" /></p>
	<p><input type="submit" text="post it !!!" /></p>
</form>
"""
print(form)
