from __future__ import division

def add(a, b):
	print "adding %d and %d" % (a,b)
	return a+b
	
def multiply(a, b):
	print "multiply %d and %d" % (a,b)
	return a*b
	
def divide (a, b):
	print "dividing %d by %d." % (a,b)
	print "I can do that in a float lol"
	return a/b 
	
def subtract (a, b):
	print "subtract %d from %d" % (b,a)
	return add (a, -1*b)

num1 = input("give a number: ")
num2 = input("give another number: ")	
	
print """
if you want to add, type a
if you want to subtract, type s
if you want to multiply, type m 
if you want to divide, type d
if you want to exit type c
"""	
resp = raw_input("what do you want to do?")
res = 0
while (resp != 'c'):
	if (resp == 'a'):
		res = add(num1, num2)
	elif (resp == 's'):
		res= subtract(num1, num2)
	elif (resp == 'm'):
		res = multiply(num1, num2)
	else:
		res=  divide(num1, num2)
	print res
	resp = raw_input("new operation: ")