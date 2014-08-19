import random
import sys

secret_number = random.randint(1,100)
actual_number = secret_number
if actual_number % 2 == 0:
	actual_number = "even"
else:
	actual_number = "odd"

user_choice = raw_input('odd or even?')

while user_choice[0] != "o" and user_choice[0]!="e":
	print "Your input was invalid. Try Again."
	user_choice = raw_input('odd or even?')
if user_choice[0] == "o" and actual_number == "odd":
	actual_number = user_choice
elif user_choice[0]=="e" and actual_number == "even":
	actual_number = user_choice

if actual_number == user_choice:
	print "You guessed it. Take some rest, no gym today."
elif actual_number != user_choice:
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