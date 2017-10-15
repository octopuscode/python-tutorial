# this is like argv

i = raw_input("enter your input, then 'c' to cancel")
iam = ""
while (i!='c'):
	iam = iam +"\n" + i
	print "%s \n" % i
	i = raw_input("next input ")
print iam
	
def print2 (*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def printnone():
	print "you gave me no arguments u ho"
	
print2 ( "cool", "beans")
printnone()
