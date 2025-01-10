#milan hill
#1/8/25
#multiplication quiz

#init
import random
import time
points = 0

#main
def mult_quiz():
    print("Welcome to the multiplication quiz! Multiply numbers correctly to earn points.")
    times = int(input("how many questions would you like for the quiz?"))
    difficulty = input("pick your difficulty: easy, medium, or hard")

    if difficulty == "easy":
        for i in range(times):
            global points
            num1 = random.randint (1,10)
            num2 = random.randint (1,10)
            product = num1 * num2
            print("the first number is: " + str (num1) + " and the second number is: " + str(num2) + " you have 5 seconds to answer.")
            start_time = time.time()
            answer = int(input("what is your answer"))
            end_time = time.time()
            elapsed_time = end_time - start_time
            if product == answer and elapsed_time < 5:
                points = points + 1
            else:
                points = points + 0
            elapsed_time = round(elapsed_time, 2)
            print(elapsed_time)


    if difficulty == "medium":
        for i in range(times):
            num1 = random.randint (1,25)
            num2 = random.randint (1,25)
            product = num1 * num2
            print("the first number is: " + str (num1) + " and the second number is: " + str(num2) + " you have 10 seconds to answer.")
            start_time = time.time()
            answer = int(input("what is your answer"))
            end_time = time.time()
            elapsed_time = end_time - start_time
            if product == answer and elapsed_time < 10:
                points = points + 1
            else:
                points = points + 0
            elapsed_time = round(elapsed_time, 2)
            print(elapsed_time)

    if difficulty == "hard":
        for i in range(times):
            num1 = random.randint (1,50)
            num2 = random.randint (1,50)
            product = num1 * num2
            print("the first number is: " + str (num1) + " and the second number is: " + str(num2) + " you have 15 seconds to answer.")
            start_time = time.time()
            answer = int(input("what is your answer"))
            end_time = time.time()
            elapsed_time = end_time - start_time
            if product == answer and elapsed_time < 15:
                points = points + 1
            else:
                points = points + 0
            elapsed_time = round(elapsed_time, 2)
            print(elapsed_time)

    print("congrats you finished the quiz! you earned " + str(points) + " points.")
    answer = input("would you like to play again?")
    if answer == "yes":
        mult_quiz()
    else:
        print("thanks for playing!")
        quit()

mult_quiz()


