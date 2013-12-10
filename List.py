#List
aList = ['first string','second string', 3, ['4th list 1/2','4th list 2/2']]
print(aList[0])
print(aList[3][1])
print(aList[:2])

aList[1] = 'second string changed!!'
print(aList)

#delete
del aList[0]
print(aList)

#append
aList.append("last value")
print(aList)

#sort : use only with same object type
bList = [6,2,5]
bList.sort()
print(bList)

#reverse
bList.reverse()
print(bList)

#insert
bList.insert(1,'test')
print(bList)

#remove
bList.remove('test')
print(bList)

#pop : get last value and remove insert
bList.pop()
print(bList)
bList.pop(0)
print(bList)

#count
print(bList.count(5))

#extend
bList.extend([1,2,3])
print(bList)

