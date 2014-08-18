import random

x = random.randint(1,100)

if x%2 == 0:
	x="even"
else:
	 x = "odd"
y = raw_input('odd or even?')
if y == "odd" or y == "o":
	if y == x:
		print "You guessed it. Take some rest, no gym today"
	else:
		print "No running away from this buddy. Go to the gym"
elif y == "even" or y == "e":
	if y == x:
		print "You guessed it. Take some rest, no gym today"
	else:
		print "No running away from this buddy. Go to the gym"