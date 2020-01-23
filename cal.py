##Performs simple arithmatic entered as a string input 
#bla bla bla

def compute(expression):
	values = expression.split(' ')

	num0 = int(values[0])
	operator = values[1]
	num1 = int(values[2])

	if operator =='+':
		return num0 + num1

	elif operator == '-':
		return num0 - num1 
	else :
		print("UNKNOWN OPERATOR")
		return None
		