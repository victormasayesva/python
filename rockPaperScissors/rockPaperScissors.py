'''
Created on May 4, 2020

@author: ITAUser
'''
import random

#set variable keepPlaying to true

keepPlaying = True

#while keepPlaying is true:

while(keepPlaying == True):

 

    #print statement welcoming players to the game

    print("Welcome to Rock Paper Scissors")

    # print statement stating the rules (best 2 out of 3 Press 'q' to quit)

    print("The game is best 2 out of 3")

    print("To quit type 'q' to quit")

    #make a key that assigns a number to each choice for the computer

    # (rock is 1, scissors is 2, paper is 3)

    

    #import random function



    #set computer's score to 0

    #set player's score to 0

    you = 0

    computer = 0

    

    #while player's score is less than 2 and computer's score is less than 2 and the player's score is less than 2:

    while (you < 2 and computer < 2):

    

        #computer's choice = random number between 1 and 3

        computerChoice = random.randint (1,3)

        #player's choice = input(ask player to select Rock, Paper, or Scissors)

        playerChoice = input("please type (rock, paper, or scissors):")

        playerChoice = playerChoice.lower()

        #if player inputs 'q' or 'Q':

        if(playerChoice == 'q'):

        #    set to keepPlayingFalse

            keepPlaying == False

        #    stop the loop

            break

        #else if (player inputs rock and computer chooses rock) or

        elif((playerChoice == "rock" and computerChoice == "1")) or ((playerChoice == "scissors" and computerChoice == "2")) or ((playerChoice == "paper" and computerChoice == "3")):

        #(player inputs paper and computer chooses paper) or

        #(player inputs scissors and computer chooses scissors):

        #   print out DRAW

            print ("DRAW")

        #   print out player's score and computer's score

            print ("Player's Score =" + you._str_() + "Computer's Score =" + computer._str_())

        #else if (player inputs rock and computer chooses scissors) or

        elif((playerChoice == "rock" and computerChoice == "2")) or ((playerChoice == "scissors" and computerChoice == "3")) or ((playerChoice == "paper" and computerChoice == "1")):

        #(player inputs scissors and computer chooses paper) or 

        #(player inputs paper and computer chooses rock):

        #   add one to the player's score

            you = you + 1

        #   print out player's score and computer's score

            print("Ya!")

            print ("Player's Score =" + you._str_() + "Computer's Score =" + computer._str_())

        #else if (player inputs rock and computer chooses paper) or

        elif((playerChoice == "rock" and computerChoice == "3")) or ((playerChoice == "scissors" and computerChoice == "1")) or ((playerChoice == "paper" and computerChoice == "2")):

        #(player inputs scissors and computer chooses rock) or

        #(player inputs paper and computer chooses scissors):

        #   add one to computer's score 

            computer = computer + 1

        #   print out player's score and computer's score

            print("Bummer!")

            print ("Player's Score =" + you._str_() + "Computer's Score =" + computer._str_())

        #else:

        #   tell the user their input was not valid





else:

    print("input not vaild")

    print("Thank you for playing Rock, Paper, Scissors")

    if(you == 2):

        print("YOU WON!!")

    if(computer == 2):

        print("Nice try, Computer Wins")

        print ("Player's Score =" + you._str_() + "Computer's Score =" + computer._str_())