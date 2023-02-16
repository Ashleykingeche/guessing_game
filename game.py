# this programme demonstrates a guessing
#game
from random import randint
# 1 get user input
user_name = input("What's your name?")

print("HELLO THERE " + user_name +"!")
# generate a random number
counter = 0
random_number = randint(10,50)
while counter < 5:
    user_number =eval(input("Enter a number:"))
    counter =+1
    if user_number < random_number:
        print("Your guess is too low")
    elif user_number >random_number:
        print("Your guees is too high")
    elif user_number == random_number:
        print("You win!")
        break
print ("Game over")
      
if user_number == random_number:
   print("You win!")
else:
    print("Game over!The correct number is ")
    print(random_number)
