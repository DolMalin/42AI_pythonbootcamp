import string
import	sys

def	is_punctuation(c):
	for x in string.punctuation:
		if c == x:
			return 1
	return 0

def text_analyzer(text):
	if not text:
		text = input("What is the text to analyze?: ")
	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
		return
	print("""The text contains {} character(s):
	- {} upper letter(s)
	- {} lower letter(s)
	- {} punctuation mark(s)
	- {} space(s)"""
	.format(len(text),
	sum(map(str.isupper, text)),
	sum(map(str.islower, text)),
	sum(map(is_punctuation, text)),
	sum(map(str.isspace, text)))
	)

if __name__=="__main__":
	if len(sys.argv) > 2:
		print("AssertionError: more than one argument")
	else:
		text_analyzer(sys.argv[1] if len(sys.argv) == 2 else None)