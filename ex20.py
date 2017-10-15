from sys import argv

fname = raw_input("name of the file you want to read")
def printall(f):
	print f.read()

def rewind(f):
	f.seek (0)
	
def println(line, f):
	print line, f.readline(),
	
current = open(fname)

print "Lets print the whole file"
printall(current)

print "lets go to the beginning and print 3 lines"
rewind(current)

curr = 1
while (curr <4):
	println(curr, current)
	curr +=1
	

