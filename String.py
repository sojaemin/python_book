print("\"This is String sample\"")
print("sample\rcode\rda~")

print("""
	change line sample
	gogo
	"""
	)

print("=="*50)
print("test")
print("=="*50)

a="this is test python code!!"
print(a[0])
print(a[-5])
print(a[0:4])
print(a[:4])
print(a[4:])

#String formating
print("test string formating %s" % "test")

#Number formating
print("test number formating %d" % 100)

#more than 2 value formating
number = 500
str_val = "five hundred"
print("sample code with two value A: %d, B: %s" %(number, str_val))

#print %
print("print fifty percent : %d%%" %50)

low = "test"
print(low.upper())
print(low.count('t'))

upper = "TEST"
print(upper.lower())

strWithBlank = "test    "
print(strWithBlank)
print(strWithBlank.rstrip()) #trim to left : lstrip(), trim to right : rstrip()

print(strWithBlank.replace("t","TTT"))

splistTest = "This is split test code!!!"
print(splistTest.split()) #split(":")

print(splistTest.swapcase()) #lower to upper, upper to lower
