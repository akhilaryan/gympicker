import random

x = random.randint(1,100)

if x%2 == 0:
	x="even"
else:
	 x = "odd"
y = raw_input('odd or even?')
if y == "odd" or y == "o" and x == "odd":
	x=y
elif y == "even" or y == "e" and x == "even":
	x=y
else:
	x!=y

if x==y:
	print "You guessed it. Take some rest, no gym today"
	
else:
	print "No running away from this buddy. Go to the gym"
	z = raw_input('Do you want me to tell you what to do in the gym?')
	if z=="yes" or z == "y":
		a = random.randint(1,3)
		if a == 1:
			print "Chest + Tricep + Shoulders"
		elif a == 2:
			print "Back + Biceps + Legs"
		else:
			print "Cardio + Abs"