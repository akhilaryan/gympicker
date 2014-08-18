import random

secret_number = random.randint(1,100)
if secret_number % 2 == 0:
	secret_number = "even"
else:
	secret_number = "odd"
user_choice = raw_input('odd or even?')

if user_choice[0] == "o" and secret_number == "odd":
	secret_number = user_choice
elif user_choice[0]=="e" and secret_number == "even":
	secret_number = user_choice
else:
	secret_number != user_choice

if secret_number == user_choice:
	print "You guessed it. Take some rest, no gym today."
	
else:
	print "No running away from this buddy. Go to the gym"
	workout = raw_input('Do you want me to tell you what to do in the gym?')
	if workout[0] == "y":
		module = random.randint(1,3)
		if module == 1:
			print "Chest + Tricep + Shoulders"
		elif module == 2:
			print "Back + Biceps + Legs"
		else:
			print "Cardio + Abs"