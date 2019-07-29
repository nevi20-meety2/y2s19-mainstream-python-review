# Part 2 of the Python Review lab.

def encode(x, y):
	if y<=1 or y>=250  :
		print("Invalid input: Outside range.")
		return None
	elif 500 >= x or x >= 1000:
		print("Invalid input: Outside range.")
		return None
	else:
		return x*y


def decode(coded_message):
	pass