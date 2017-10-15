from sys import argv
from os.path import exists

script, fromf, tof = argv; 

print "copying data from %s to %s" % (fromf, tof)

indata = open(fromf).read()

print "the input file is %d bytes and in binary that is %s" % (len(indata), bin(len(indata)))
print "does the output file exist? %r" % exists(tof)
print "hit RETURN to continue, hit CTRL-C to abort"
raw_input()

out_file = open(tof, 'w')
out_file.write(indata)

print "all done"

print out_file.read()

out_file.close()
