import re

def convert(string):
	out = ''
	for n in string:
		if re.match(r'[a-z]', n):
			out += char(n, 'a')
		elif re.match(r'[A-Z]', n):
			out += char(n, 'A')
		else:
			out += n
	return out
	
def char(letter, base):
	return chr((((ord(letter) % ord(base)) + 13) % 26) + ord(base))
	
def test():
	string = 'the quick fox jumped over the lazy brown dog'
	string == convert(convert(string))
	string = string.capitalize()
	string == convert(convert(string))
	
	string = '<html> test !@#$%^&*()</html>'
	string == convert(convert(string))
	print "All Tests Pass!"
	print "Perhaps you should make more tests?"