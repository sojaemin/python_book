#file
fileA = open("c:/new.txt","w") #r : read w:write a:add at last
fileA.close()

#write mode
fileA = open("c:/new.txt","w")
for i in range(1,11):
	data = "==%d==\n" % i
	fileA.write(data)

fileA.close()

#read 1 line
fileA = open("c:/new.txt","r")
readLine = fileA.readline()
print(readLine)
fileA.close()

#read all with readline()
fileA = open("c:/new.txt","r")
while 1:
	readLine = fileA.readline()
	if not readLine: break
	print(readLine)
fileA.close()

#read all with readlines()
fileA = open("c:/new.txt","r")
readLines = fileA.readlines()
for rline in readLines:
	print(rline)
fileA.close()

#read all with read()
fileA = open("c:/new.txt","r")
data = fileA.read()
print(data)
fileA.close()

#add mode
fileA = open("c:/new.txt","a")
for i in range(11,20):
	data = "==%d==\n" % i
	fileA.write(data)
	print(fileA.tell()) #tell : get point
fileA.close()

#tell/seek
fileA = open("c:/new.txt","a")
fileA.seek(0) #seek : set Point

