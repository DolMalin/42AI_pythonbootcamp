import sys

def	convert_nbr(input):
	if not input.replace(".", "", 1).isdigit():
		return None
	try:
		nb = int(input)
	except ValueError:
		nb = float(input)
	return nb		

def	do_op(a, b, op):
	if a is None or b is None:
		return "ERROR (only digits)"
	if op == '+':
		return a + b
	if op == '-':
		return a - b
	if op == '*':
		return a * b
	if op == '/' and b != 0:
		return a / b
	if op == '/':
		return "ERROR (division by zero)"
	if op == '%' and b != 0:
		return a % b
	if op == '%':
		return "ERROR (moduly by zero)"

if len(sys.argv) > 3 or len(sys.argv) < 2:
	print("AssertionError: too or few arguments")
else:
	a = convert_nbr(sys.argv[1])
	b = convert_nbr(sys.argv[2])

print(
"""
Sum:		{}
Difference:	{}
Product:	{}
Quotient:	{}
Remainder:	{}
"""
	.format(
	do_op(a, b, '+'),
	do_op(a, b, '-'),
	do_op(a, b, '*'),
	do_op(a, b, '/'),
	do_op(a, b, '%'),
	)
)
