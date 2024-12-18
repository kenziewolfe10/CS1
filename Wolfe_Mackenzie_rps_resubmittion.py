#cat
import os
import random
import time
possible_actions = ["rock", "paper", "scissors"]                                     #This is a list of the possible actions for the computer to choose from
while True:                                                                          #forever loop
    player1_score = 0                                                                #starts player 1 scores to 0
    player2_score = 0                                                                #starts player 2 scores to 0

    while player1_score < 3 and player2_score < 3:                                   #do this forever loop when player 1 and 2 scores are below 3 points
        play_style = str.lower(input("Play with 2 players or play with robot? "))    #asks user if there playing with 2 players or with the robot
        player1 = str.lower(input("rock, paper, or scissors? "))                     #This dispays the question for the user to response, allows the user to use capital letters

        if play_style == "2":                                                        #if the user picks 2 players
            os.system('cls')                                                         #clearing the screen
            player2 = str.lower(input("rock, paper, or scissors? "))                 #display "rock, paper, or scissors?"
            os.system('cls')                                                         #clearing the screen
        elif play_style == "robot":                                                  #if the user picks to play with robot
            player2 = random.choice(possible_actions)                                #This tells the computer to randomly pick an action from the list above

        time.sleep (2)                                                               #pauses code for 2 seconds
    
        if player1 == player2:                                                       #if what the user says is also what the computer picks
            print("It's a tie")                                                      #display "it's a tie"
        elif player1 == "paper" and player2 == "rock":                               #if the user says paper and the computer picks rock
            print("Paper beats rock. Player 1 wins!")                                #display "Paper beats rock. Player 1 wins!"
            player1_score+=1                                                         #adds a point to player 1 score
        elif player1 == "rock" and player2 == "scissors":                            #if the user says rock and the computer picks scissors 
            print("Rock beats scissors. Player 1 wins!")                             #display "Rock beats scissors. Player 1 wins!"
            player1_score+=1                                                         #adds a point to player 1 score
        elif player1 == "scissors" and player2 == "paper":                           #if the user syas scissors and the computer picks paper
            print("Scissors beats paper. Player 1 wins!")                            #display "Scissors beats paper. Player 1 wins!"
            player1_score+=1                                                         #adds a point to player 1 score
        elif player1 == "scissors" and player2 == "rock":                            #if the user says scissors and the computer picks rock
            print("Rock beats scissors. Player 2 wins!.")                            #display "Rock beats scissors. Player 2 wins!"
            player2_score+=1                                                         #adds a point to player 2 score
        elif player1 == "paper" and player2 == "scissors":                           #if the user says paper and the computer picks scissors
            print("Scissors beats paper. Player 2 wins!")                            #display "Scissors beats paper. Player 2 wins!"
            player2_score+=1                                                         #adds a point to player 2 score
        elif player1 == "rock" and player2 == "paper":                               #if the user says rock and the computer picks paper 
            print("Paper beats rock. Player 2 wins!")                                #display "Paper beats rock. Player 2 wins!"
            player2_score+=1                                                         #adds a point to player 2 score
        else:                                                                        #if the user says anything other than the list
            print("Invalid response")                                                #display "Invalid response"
    
        print(f"Player 1 has {player1_score} point. Player 2 has {player2_score} points.")  #print player 1 and player 2 scores

    if player1_score == 3:                                                           #if player 1 score is 3
        print ("player 1 wins the game!")                                            #print "player 1 wins the game"
        exit()                                                                       #exits code
    elif player2_score == 3:                                                         #if player 2 score is 3
        print ("player 2 wins the game!")                                            #print "player 2 wins the game!"
        exit()                                                                       #exits the forever loop
    while True:                                                                      #forever loop
        play_again = input("Play again?")                                            #creates variable for play again and asks the user to play again
        if play_again == "yes":                                                      #if they say yes to play again
            print("ok... playing again")                                             #print "ok... playing again" and resart code
            break                                                                    #stops the forever loop
        elif play_again == "no":                                                     #if they say no to play again
            print("Bye!")                                                            #print "bye"
            exit()                                                                   #exits forever loop
        else:                                                                        #if anything other than yes or no
            print("invalid response")                                                #print "invalid response"