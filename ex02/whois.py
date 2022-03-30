import sys

if len(sys.argv) < 2:
	print("AssertionError: no argument")
elif len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif not sys.argv[1].isdigit():
	print("AssertionError: argument is not an integer")
elif int(sys.argv[1]) % 2 == 0:
	print("I'm Odd.")
elif int(sys.argv[1]) % 2 != 0:
	print("I'm Even.")
else:
	print("I'm Zero.")