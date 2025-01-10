#guessing game
print ("welcome to the guessing game , guess a number betweem 1 and 10")

import random
guess= int(input("Enter Number"))
secret=random.randint(0,10)
if guess==secret:
    print ("you have guessed the number")

if guess>secret:
    print ("Your guess was too high the correct number is " + str(guess) + " would you like to play again?")
    ans= input("Yes")
    if ans == "Yes":
        print ("great! pick an integer between 1 and 10" )
        guess= int(input("Enter Number"))
        secret=random.randint(0,10)
        if guess==secret:
            print ("you have guessed the number!!!!")
        else:
            print ("sorry thats wrong, thanks for playing")
    else:
        print ("thanks for playing <3")

if guess<secret:
    print ("your guess was too high the correct number is " + str(guess) + " would you like to play again?")
    ans= input("Yes")
    if ans == "Yes":
        print ("great! pick an integer between 1 and 10" )
        guess= int(input("Enter Number"))
        secret=random.randint(0,10)
        if guess==secret:
            print ("you have guessed the number!!!!")
        else:
            print ("sorry thats wrong, thanks for playing")
    else:
        print ("thanks for playing <3")


#make sure both variables integers
