#if
testval1 = "1"
if testval1:
	print("yes")
else:
	print("no")

#or, and, not
if not testval1 or "1":
	print("A")
else:
	print("B")	

testval2 = "sojaemint"
#in
if "t" in testval2: #can use string, list, tuple
	print("T")
else:
	print("No T")

#not in
if "t" not in testval2:
	print("T")
else:
	print("No T")

#elif
if "d" in testval2:
	print("D")
elif ("t" in testval2):
	print("T")
else:
	print("No T")

#pass
if "t" in testval2: #can use string, list, tuple
	pass
else:
	print("No T")

#
if "t" in testval2 :print("last T")
else:
	pass