formatter = ' %r %r %r %r '

print formatter %(1,2, "three", "four")
print formatter % (
'yo', 'this my shit', 'all the boys', 'want a piece of this')

print """
I am a beautiful
butterfly
made of 
butter"""

print '''
this is what
i like to 
type 
'''


while True:
	for i in [ "\ " "-" "|"]:
		print "%s\r" % i