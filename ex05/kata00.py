kata = (19,42,21)

def	check_kata(elem):
	for x in elem:
		if not isinstance(x, int):
			return False
	return True

def	join_tups(elem):
	return ', '.join(map(str, elem))

def	print_kata(elem):
	if not check_kata(elem):
		print("ERROR (only integers)")
	print("The {} numbers are: {}"
	.format(len(kata), join_tups(elem)))

print_kata(kata)
