num = 10
dont = "don't"
c = "there are %d types of people" % num
d = "those who understand binary and those who %s" %dont


print c
print d
print "i said %s and %s" % (c,d)

print "isn't that funny?"
print "there are %s types of people, but in binary lol" % bin(num)

hilarious = False

jokeeval = "isn't that joke hilarious? %r"

print jokeeval % hilarious