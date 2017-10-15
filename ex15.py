from sys import argv
script, filename = argv

txt = open(filename)

print "here's your file, named %r" % filename
print txt.read()

file_again = raw_input("type the filename again >")

print "We're going to erase %r" % file_again
print "if you don't want to do that, hit CTRL - C"
print "if you do want to do that , hit return"

raw_input("what do you want to do?")
target = open(file_again, 'w')

print "truncateating (deleting the contents of ) the file. DO IT!"
#target.truncate()

print "I want to ask you for three lines to fill the file with"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write \n %r \n %r \n %r to the file" % (line1,line2,line3) 

target.write(line1)
target.write("\n") 
target.write(line2)
target.write("\n") 
target.write(line3) 
target.write("\n") 

print "and now i will close it"
target.close()