def add(a, b):
	print "Adding %d + %d " %(a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d " %(a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %d " %(a, b)
	return a * b

def divide(a, b):
	print "Divideing %d / %d " %(a, b)
	return a / b

print "Let's us do some math with just function"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, Divide: %d" %(age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "can you di it by hand"
