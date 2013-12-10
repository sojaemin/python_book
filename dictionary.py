#dictionary
dic01 = {'str1':'first string','str2':'second string', 'str3':'third string'}
print(dic01['str2'])
dic01['str2'] = 'second string changed!!!'
print(dic01['str2'])

#add
dic01['str4'] = '4th string'
print(dic01)

#delete
del dic01['str1']
print(dic01)

#keys
print(dic01.keys())

for x in dic01.keys():
	print('=='+x+'=='+x)

#get Dict_keys as list
print(list(dic01.keys()))

#get values
print(dic01.values())

#get items
print(dic01.items())

#get
print(dic01.get('str2'))
print(dic01.get('str5','default value'))

#has items
print('str5' in dic01)
print('str2' in dic01)

#clear
dic01.clear()
print(dic01)
