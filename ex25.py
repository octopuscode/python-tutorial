def breakbyword(stuff):
	"""delimit by space"""
	words = stuff.split(' ')
	return words

def breakbycomma(stuff):
	phrase = stuff.split(',')
	return phrase
	
def sort_words(words):
	"""this sorts the words fool"""
	return sorted(words)

def print1stword(words):
	word = words.pop(0)
	print word
	
def printlastword(words):
	word = words.pop(-1)
	print word
	
def sortsentence(sentence):
	words = breakbyword(sentence)
	return sort_words(words)
	
def printfirstandlast(sentence):
	words = breakbyword(sentence)
	print1stword(words)
	printlastword(words)
	
def printalf1standlast(sentence):
	words = sortsentence(sentence)
	print1stword(words)
	printlastword(words)
	
