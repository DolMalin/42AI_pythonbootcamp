kata = (2019, 9, 25, 3, 30)

def	check_kata(elem):
	if len(elem) != 5:
		return False
	for x in elem:
		if not isinstance(x, int) or x < 0:
			return False
	if len(str(elem[0])) > 4:
		return False
	for x in elem[1:]:
		if len(str(x)) > 2:
			return False
	return True

def	format_kata_elem(c):
	if len(str(c)) < 2:
		return '0' + str(c)
	else:
		return str(c)

def	format_kata(elem):
	date = format_kata_elem(elem[1]) + '/'
	date += format_kata_elem(elem[2]) + '/'
	date += format_kata_elem(elem[0]) + ' '
	date += format_kata_elem(elem[3]) + ':'
	date += format_kata_elem(elem[4])
	return date

def	print_kata(elem):
	if not check_kata(elem):
		return print("ERROR: Wrong numbers format")
	return print(format_kata(elem))

print_kata(kata)