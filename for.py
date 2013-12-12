#for
listA = [1,2,3]
for x in listA:
	print(x)

#continue
for x in listA:
	if x == 1:
		continue
	print(x)

#range
rangeA = range(10) #or range(10,20) etc

print(rangeA)

sum = 0
for i in range(1,11):
	sum += i

print(sum)

#
for k in range(len(listA)):
	if listA[k] == 1:
		continue
	print(listA[k])

#use tuple
tupleA = [(1,2), (3,4), (5,6)]
for (a,b) in tupleA:
	print(str(a)+":"+str(b))

