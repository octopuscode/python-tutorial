from sys import argv

script, username = argv
prompt = '>'

print "hi %s i am the %s script" % (username, script)
print "i'd like to ask you questions because i'm nosy"
print "do you like me %s?" %username
likes = raw_input(prompt)

print """

when i asked if you liked me, you said %r
you son of a bitch, %r
""" % (likes, username)