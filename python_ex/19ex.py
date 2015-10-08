"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket!\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Oh, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""

def function(x, y):
	print "x + y = %d" % (x + y)
	print "x = %d, y = %d" % (x, y)
	print "x * y = %d" % (x * y)
	print "**********"

a = 1;
b = 1;

function(2, 3)
function(3, 4)
function(4, 5)
function(4 + 1, 5 + 1)
function(2 * 3, 3 * 4)
function(2 < 3, 3 < 2)
function(a, b)
function(a < b, a == b)
