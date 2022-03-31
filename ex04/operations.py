import sys

if len(sys.argv) > 3 or len(sys.argv) < 2:
	print("AssertionError: too or few arguments")
else:
	a = int(sys.argv[1])
	b = sys.argv[2]
	print(isinstance(a, int))