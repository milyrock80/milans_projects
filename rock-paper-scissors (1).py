#Milan Hill
#1/6/2025
#Rock Paper Scissors

#init
wins = 0
loses = 0
ties = 0
#functions
#main

def rps ():
    global wins
    global loses
    global ties
    import random
    print("Welcome to Rock Paper Scissors!")
    player_choice = (input("Pick your move choice, either rock, paper or scissors"))
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
       player_choice = input("please retry your input! Pick your move choice, either rock, paper or scissors")

    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "paper"
    if computer_choice == 2:
        computer_choice = "rock"
    if computer_choice == 3:
        computer_choice = "scissors"

    if player_choice == "rock" and computer_choice == "scissors":
        print("you win!")
        wins = wins + 1
        loses = loses + 0
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins." + " You have " + str(loses) + " loses. " + " You have " + str(ties) + " ties. " )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "scissors" and computer_choice == "rock":
        print("computer wins!")
        wins = wins + 0
        loses = loses + 1
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins." + " You have " + str(loses) + " loses. " + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "paper" and computer_choice == "rock":
        print("you win!")
        wins = wins + 1
        loses = loses + 0
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins." + " You have" + str(loses) + " loses. " + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "rock" and computer_choice == "paper":
        print("computer wins!")
        wins = wins + 0
        loses = loses + 1
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins." + " You have " + str(loses) + " loses." + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "scissors" and computer_choice == "paper":
        print("you win!")
        wins = wins + 1
        loses = loses + 0
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins." + " You have " + str(loses) + " loses. " + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "paper" and computer_choice == "scissors":
        print("computer wins!")
        wins = wins + 0
        loses = loses + 1
        ties = ties + 0
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " win(s)" + " You have " + str(loses) + " loses." + " You have " + str(ties) + " tie(s).")
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "paper" and computer_choice == "paper":
        print("tie!")
        wins = wins + 0
        loses = loses + 0
        ties = ties + 1
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " win(s) " + " You have " + str(loses) + " loses." + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "rock" and computer_choice == "rock":
        print("tie!")
        wins = wins + 0
        loses = loses + 0
        ties = ties + 1
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins. " + " You have " + str(loses) + " loses." + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")
    if player_choice == "scissors" and computer_choice == "scissors":
        print("tie!")
        wins = wins + 0
        loses = loses + 0
        ties = ties + 1
        print("you chose " + str(player_choice) + " and the computer chose " + str(computer_choice) + "." + " You have " + str(wins) + " wins. " + " You have " + str(loses) + " loses." + " You have " + str(ties) + " ties." )
        repeating_game = input("would you like to play again?")
        if repeating_game == "yes":
            rps()
        if repeating_game == "no":
            print("thanks for playing!")

rps()
