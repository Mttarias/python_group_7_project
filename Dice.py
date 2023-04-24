#Create Random Numbers in order to simulate a dice roll
import random

# Initialise player socres to number 0
player1_score= 0
player2_score= 0

#Repeat everything in this block 12 times
for i in range (12) :

    # Generate random numbers between 1 and 6 for each player.
    player1_value= random.randint(1,6)
    player2_value = random.randint(1,6)

    #Display the values
    print("Player 1 rolled: ", player1_value)
    print("player 2 rolled: ", player2_value)

    # Pick: take the appropriate path through the code and base them on the comparison of the values.
    if player1_value > player2_value:
        print("player 1 wins.")
        player1_score = player1_score + 1 # adds variable
    elif player2_value > player1_value:
        print("player 2 wins")
        player2_score = player2_score +1
    else: 
        print("It's a tie")

    input("Press enter to continue.") # Wait for user input to proceed.


print("### Game over ###")
print("Player 1 score:", player1_score)
print("Player 1 score:", player2_score)







