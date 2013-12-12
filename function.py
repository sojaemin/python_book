#function
def sum(a,b):
	return a+b

print(sum(2,4))

def printHi():
	print("HI")

print(printHi())

#lot's parameters
def sum_alot(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print("=="+str(sum_alot(3,5,3,4,5,6)))

#2 return = return tuple
def sum(a,b):
	return a,b

print(sum(2,4))

#init
def sum(a,b,c=100):
	return a,b,c

print(sum(2,4))
print(sum(2,4,6))
