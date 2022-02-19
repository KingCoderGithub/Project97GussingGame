import random

print("Welcome to Guessing Game")

number = random.randint(1,9)

chances = 0
 
print ("Guess a number (between 1 and 9) :")

while chances < 5 : 
    guess = int(input("enter your guess:"))
    if guess == number:
        print("Congrats! you win")
        break
    elif guess < number :
        print("Too Low, Guess a higher number")
    else :
        print("Your guess was too high, guess a smaller number")
        
    chances += 1
if not chances < 5 :
    print ("You lose!")
