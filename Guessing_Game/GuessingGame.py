''' Guessing Game Challenge
Let's use while loops to create a guessing game.
The Challenge:
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is 
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

#START


#Computer's Number Selection;
from random import randint
comp_num=randint(1,100)


#Description of rules;
print("Let's Play a guessing game!")
input() #THIS INPUT WILL WORK LIKE getch() IN C++; we just have to press enter!
print("RULES:")
print("1. Computer will select a number.")
print("2. You have to guess it!")
print("""3. On a your first turn, if your guess is
within 10 of the number, "WARM! will be printed."
further than 10 away from the number, "COLD!" will be printed.""")
print("""4. On all subsequent turns, if your guess is 
closer to the number than the previous guess,"WARMER!" will be printed.
farther from the number than the previous guess, "COLDER!" will be printed.""")
input() 
print("READY? LET'S BEGIN!!!")
input() 


#LOGIC;
import math
count=1
user_guess=0

while(user_guess!=comp_num):

	while(1>user_guess or user_guess>100):
		user_guess=int(input("Enter Your Guess: "))
		if 1>user_guess or user_guess>100:
			print("OUT OF BOUNDS")

	temp=abs(user_guess-comp_num)

	#if the guess is within 10;
	if temp<=10: 
		if(count==1):
			print("WARM!")
		else:
			print("WARMER!")
	#if guess is farther than 10;
	else:
		if(count==1):
			print("COLD!")
		else:
			print("COLDER!")

	user_guess=int(input("Enter Your Guess: "))
	count+=1

	#WHILE LOOP ENDS;

print(f'CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER {comp_num} IN {count} ATTEMPTS!')
#Printing final statement using f-strings method;


#END






