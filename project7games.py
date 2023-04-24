import sys
import random

#A dictionary used to keep track of users discovered endings
endings = {"good end" : 0, "evil end" : 0, "died" : 0, "secret end" : 0}
#A dictionary used to keep track of players score in the rock paper scissor game
rpsScore = {"win": 0, "loss": 0, "tie": 0}

#Main menu, access the three different games and display extras
def menu():
    choice = 0
    while choice < 1 or choice > 6:
        print("""
        1. Text Adventure
        2. Dice
        3. Rock Paper Scissor
        4. Display Text Adventure endings
        5. Display Rock Paper Scissor score
        6. Exit
        """)
        try:
            #match/case menu for user to select, each case leads to the function for a game or display
            choice = int(input("Enter your selection: "))
            match choice:
                case 1:
                    startPath()
                case 2:
                    diceGame()
                case 3:
                    rockPaperScissor()
                case 4:
                    printEndings()
                case 5:
                    printRpsScore()
                case 6:
                    sys.exit()
                case _: #default case, if user inputs any integer other than 1, 2, 3, 4, 5 or 6
                    print("Please make a valid selection")
        except ValueError: #Catches invalid user input, if user did not enter an integer
            print("Please enter a number.")

def diceGame():
    # Initialise player scores to 0
    diceScores = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Ties": 0}
    p1Wins = "Player 1 Wins"
    p2Wins = "Player 2 Wins"

    #Repeat everything in this block 12 times
    for i in range (12) :

        # Generate random numbers between 1 and 6 for each player.
        player1_value= random.randint(1,6)
        player2_value = random.randint(1,6)

        #Display the values
        print("Player 1 rolled: ", player1_value)
        print("Player 2 rolled: ", player2_value)

        # Pick: take the appropriate path through the code and base them on the comparison of the values.
        if player1_value > player2_value:
            print(p1Wins)
            diceScores[p1Wins] += 1
        elif player2_value > player1_value:
            print(p2Wins)
            diceScores[p2Wins] += 1
        else: 
            print("It's a tie")
            diceScores["Ties"] += 1

        input("Press enter to continue.") # Wait for user input to proceed.

    #Print scores
    for player, wins in diceScores.items():
        print(player, ":", wins, end=" ")
    
    #return to menu
    gameOver()


def rockPaperScissor():
    #Game: Rock, Paper, Scissors
    possible_actions = ("rock", "paper", "scissors")

    #User will input selection
    user_action = input("Enter a choice (rock, paper, scissors): ")
    user_action = user_action.lower()
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    #User versus computer; outcome is printed and result is tracked
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        rpsTie()
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            rpsWin()
        else:
            print("Paper covers rock! You lose.")
            rpsLoss()
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            rpsWin()
        else:
            print("Scissors cuts paper! You lose.")
            rpsLoss()
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            rpsWin()
        else:
            print("Rock smashes scissors! You lose.")
            rpsLoss()
    else:
        print("Invalid entry, try again!")

    #Return to menu once game is finished
    gameOver()


#Three functions to update the rps score
def rpsWin():
    rpsScore["win"] += 1

def rpsLoss():
    rpsScore["loss"] += 1

def rpsTie():
    rpsScore["tie"] += 1


#Print rock paper scissor score
def printRpsScore():
    for win, result in rpsScore.items():
        print(win, ":", result, end=" ")
    print()
    menu()
        

#Function for players to choose option 1 or 2 during text adventure
def selectPath():
    while True:
        #Validates user input by throwing a value error exception in the event that the user enters a non integer as an input
        try:
            choice = int(input("To select the first option enter 1, to select the second option enter 2. Choose wisely\n"))
            match choice:
                case 1 | 2:
                    return choice
                case _: #default case, if user inputs any integer other than 1 or 2
                    print("Please make a valid selection")
        except ValueError:
            print("Please enter an integer")


#Returns players to the main menu after completing a game
def gameOver():
    print("Game over, press enter to return to menu")
    input()
    menu()


#At the end of each ending, function prints the current endings achieved looping through the dictionary
def printEndings():
    for ends, amounts in endings.items():
        print(ends, ":", amounts, end=" ")
    print()
    menu()


#Checks the type of ending the player achieved
def adventureResult(end):
    if end in endings: #Checks if argument is good end or evil end 
        endings[end] += 1
    else:
        print("Congratulations you found a secret end")
        endings["secret end"] += 1

    input("Press enter to return to the main menu")
    menu()


#Tracks character deaths
def adventurerDied():
    endings["died"] += 1


#Function for players to select which initial path they will choose
def startPath():
    print("""
        Heroes distinguish themselves through their primary attribute, namely: Strength, Intelligence and Charisma.
        What do you covet young adventurer? The decisions you make will alter the destiny that awaits you.
        (Please enter strength to begin your adventure. Intelligence and charisma will be available in a future update)
        """)
    #Loops until player makes a valid choice, either strength or charisma
    while True:
        pathSelection = input()
        match pathSelection.lower():
            case "strength":
                strengthPath()
            case "intelligence":
                print("Intelligence is currently unavailable, please make another selection.")
            case "charisma":
                print("Charisma is currently unavailable, please make another selection.")
            case _: #Default case, if the user does not input one of the three strings or makes a spelling error when doing so
                print("Please check your spelling or make a valid selection.")


#Holds all of the strength path choices
def strengthPath():
    print("""
        You have always placed physical strength above all other wordly pursuits, potentially a little too much but
        who am I to judge. *clears throat*
        You find yourself where you always are, the gym. *sigh* After all these years with no one to spot you while 
        you bench press alot of weight, you continue your workouts with little effort and feeling a void inside 
        yourself. The joy the weights have brought you has diminished to almost nothing after all these years. Maybe
        you could go out and find a party to adventure into the wilds with? You don't have to of course but I feel 
        like you should, what do I know. 
        (You have two choices, the first of many crossroads you will find)
        """)
    firstChoice = selectPath()

    #Player chose to find a party
    if firstChoice == 1:
        print("""
        You decide to head to the adventure quest board hoping to find a notice of a party looking for members.
        As you approach the board you see a couple of adventurers standing near it. They notice you, mostly due to your
        size. "Ho there friend, are you looking to join a party?" you look at one of them and then the other. You decide
        to seize this opportunity and give an affirmative grunt... wow ok. "Amazing, I have some, uh, interrogation I need
        to do at a tarvern nearby and need somebody with me. My friend here has other work to do and wouldn't mind some help
        with her books?" the slightly larger man points to the sack of books. He looks back at you expectingly.
        """)
        choiceParty = selectPath()

        #Player chose to go to the tavern with bard
        if choiceParty == 1:
            print("""
            You feel you look intimidating enough, and you're correct. I'm glad some of the comments I make go over your head
            otherwise I'd be more quiet. Anyway you arrive at the tavern with your new party member, you scan the room looking
            for potential threats, you see an arm wrestling competition in the corner and before you can move towards it your 
            friend is pulling you along towards the bar. You spend an hour or two being a wingman to your companion as you
            watch him sweet talk anyone in his vicinity, before long you are edged out by the small crowd gathered around him.
            Fortunately the arm wrestling thing is still happening, as you are making your way there you hear a thud coming
            from upstairs. Now you could just ignore the sound and arm wrestle or you could go upstairs to investigate I suppose.
            """)
            choiceTavern = selectPath()

            #Player chose to arm wrestle
            if choiceTavern == 1:
                print("""
                After a couple of hours beating anyone who challenged you, the tavern owner approaches you. Smiling wide at you,
                "I have a proposition for you, work for me in this tavern helping out and accepting arm wrestling challenges
                and I will pay you a living wage and 30 percent of the winnings from the arm wrestling." His smile never faded from
                his face, like he has been staring down a gold mine he just discovered. You feel his will is too strong for any other
                answer but yes. So the years pass you by as you meet new people and never lose a single arm wrestling challenge.
                Living in relative comfort in an apartment above the tavern, always wondering what could've been.
                """)
                gameOver()

            #Player chose to investigate noise upstairs
            else:
                print("""
                You work your way up the stairs, surprinsingly nimble for a person of you size. The third door on your left you notice
                is slightly ajar. Inside you find the king of the country lying in a pool of his own blood, standing over him a shadowy
                figure wielding glistening metal. Before your brain can finish processing the scene the figure sees you and escapes out
                the window. Your first instict is to chase down the assassin, but your eyes find the illegal things in the room. You
                could chase down the assassin or you could instead clean up after the king and report this to the council.
                """)
                choiceUpstairs = selectPath()

                #Player chose to chase down the assassin
                if choiceUpstairs == 1:
                    print("""
                    You were good up until the very end, you feel the cold, hard ground underneath your face. Confused as to what exactly
                    happened. Honestly so am I, those guys were crazy fast. At least I think it was more than one.
                    """)
                    adventurerDied()
                    gameOver()

                #Player chose to cover up for the king
                else:
                    print("""
                    Not your most honest work, definitely. Regardless, the council thanked you very much for your discretion. So much
                    that you are now minor nobility, given some land to west for your silence in this embarrasing incident. Maybe not
                    the adventure you wanted but its a nice ending, kinda.
                    (Congratulations you found the morally questionable ending!)
                    """)
                    adventureResult("win?")

        #Player chose to carry books for the wizard
        else:
            print("""
            You lean over and pick the relatively light sack, the smaller one looks up to you with a half disinterested smile. 
            "Thank you, this way" you realize after your new companion spoke that she sounds much older. Its hard to tell age
            underneath all that cloth and wizards hat. You spend most of your day fetching books and hauling them around. You 
            feel it has been mostly wasted, boredom even drove you to glance at some of the wizards books. She seems very pleased
            with your help and offers you to apprentice under her as a novice mage. Would you like to accept her offer or maybe
            get in a party wasn't the best idea after all and you feel like you would rather go back to being on your own and 
            look for something else to do?
            """)
            choiceBooks = selectPath()

            #Player chose to apprentice under the wizard
            if choiceBooks == 1:
                print("""
                You slowly lose your muscle mass as you end up a scribe and book hauler for the young wizard, she is kind and you enjoy
                her company most of the time. One day a great demon lord attacks the city you reside in, the destruction catching you off
                guard, you fall unconcious. Several hours later your master wakes you up as she has finished healing your wounds, she looks
                like she's been through a tough fight and you come to find out that she single handedly destroyed the demon lord and healed
                some citizens and she is heralded as a great hero. I guess being near greatness is better than nothing... right?
                """)
                gameOver()
            
            #Player chose to try adventuring on his own outside
            else:
                print("""
                You say your goodbyes to the wizard, she doesn't seem to show much emotion at your leaving. As you walk outside you see a
                crowd gathered by the center of the square, you over hear some person shouting about destiny and swords, you even catch a
                glimpse of one by the orator, and- what do you mean you don't know what an orator is? *sigh* a speaker, better? anyway, you
                also feel a strange pull towards a water fountain which is much less crowded, and you feel a warmth coming from your pants.
                No not that, it's a coin the wizard gave you, you think it wants you to toss it into the fountain but that sword looks so shiny.
                Do you want to toss the coin or pull the sword?
                """)
                choiceTownSquare = selectPath()
                
                #Player chose to toss the coin into the fountain
                if choiceTownSquare == 1:
                    print("""
                    The last thing you remember is the coin hitting the water, and the ripples moving away from the point of impact and then
                    continuing to ripple through your vision. You are sitting up in a comfortable bed, skin glistening with sweat, and you
                    feel a shifting as you notice your partner asleep next to you. You feel confused for a few minutes as reality brings 
                    your senses back to you. It was just a very long and weird dream, you shake your head to yourself as you lay down once
                    again, catching a slightly glowing coin out of the corner of your eye, on the floor of the room. Which looks almost
                    exactly like the one in your dream...
                    (Congratulations you found the total recall ending!)
                    """)
                    adventureResult("total recall")

                #Player chose the old sword in the stone trick
                else:
                    print("""
                    You wait in line for your turn, while every tom, richard and harry take their turns trying to pry out this sword out of
                    the ground. They really need more diverse names in this town. Finally your turn comes up, you take a step forward and
                    place your hand on the gilded hilt of the sword. The sword comes out with ease and as everyone stares at you in wonder
                    a loud explosion tears through buildings to your left as you watch a figure in yellow levitates out of the rubble and
                    points at you. A name flashes in your head, "King in Yellow". The fight takes a while as you try to divert this creatures
                    attacks away from the fleeing citizens, but finally with one fell swoop you loop the entities head off. The city cries in
                    victory and heralds you the hero king of the century. Not bad for just taking a sword out of the ground eh? 
                    """)
                    adventureResult("good end")
    #Player chose to go at it alone
    else:
        print("""
        Okay maybe not adventuring but there has to be something you can do to get a little human interaction right?
        Now let's see what could I suggest for you to do, hmmmm. Oh I see a notice by that building, it says "Strong reliable
        men wanted for the city watch, equipment will be provided for new recruits" and theres a picture of a heavily clad
        warrior pointing at you with a quote that reads "We want you" not the best option sure but It's something. Oh and over
        there across the street there is an elderly gentleman who seems to be having difficulty moving his piano into his
        home, cut right through the bureacracy and help your fellow man right away. So would you like to join the city watch
        or help the elderly gentleman?
        """)
        choiceNoParty = selectPath()

        #Player chose to join the (nights) watch, something about guards! guards!
        if choiceNoParty == 1:
            print("""
            The watch becomes your family over time, you find yourself one at 56 years old and retiring in a year. You've had a happy
            and fulfilling life in this time, making the best decision you think you could've made. Adventuring is often dangerous and
            there is nothing better than job stability and a salary... right?
            """)
            gameOver()

        #Player chose to help out his fellow man right away
        else:
            print("""
            The only challenge you face when single handedly moving the piano is a geometric one, essentially fitting a triangle in a
            square hole. The laws of physics never stopped you or your muscles before so after an hour you finally finish, with a singular
            bead of sweat forming on your forehead. The elderly man provides you with freshly baked bread and probably the best lemonade
            you've ever had, seriously it's amazing. He pats your strong muscles and says "I appreciate all your help young'un, if you'd
            like there is an old crypt that belonged to my family for generations, there should still be some treasure there" ... wow
            that's crazy! did you hear him!? he said young'un, apostrophe and all. I didn't think anyone still alive used that word.
            Anyway on your way out of his home, someone stops you and offers you a bodyguard position. You could go look for some potential
            treasure or you can just take the sure thing and accept the job offer.
            """)
            choiceHelpElderly = selectPath()
            
            #Player chose to look for the treasure in the crypt
            if choiceHelpElderly == 1:
                print("""
                You find yourself a few hours outside of town, a crypt entrance set against the face of a nearby rock. Before you can get closer
                a shadowy figure steps out of the entrance, stops and looks over at you. "If you are here for the treasure I have not taken
                it, you are free to take it for yourself so long as you do not stand in my way." The figure appraises you once more and begins
                walking towards the city you came from, giving a sickengly evil aura. The persons intentions are pretty clear to you, if you let
                the creature pass they will bring death and destruction to the town. If you choose to stand in their way you might be able to stop
                them but you will not leave the battle alive. Do you want to risk your life to potentially save thousands or would you rather not
                put your neck on the line?
                """)
                choiceCrypt = selectPath()
                
                #Player chose to sacrifice themselves for the greater good
                if choiceCrypt == 1:
                    print("""
                    The battle is not even, and still you fight with everything ounce of your strength while carrying the fates of thousands of people
                    on your back. As the pain and wounds become too much you feel yourself slipping, with one last push you manage to land a final strike
                    on the creature. It wails its death cry as both you and it perish by the foot of the entrance to the crypt.
                    """)
                    adventurerDied()
                    adventureResult("good end")

                #Player chose to stand aside and look for their treasure
                else:
                    print("""
                    You warily watch the creature head towards the town, once it is out of view you head inside the crypt and find your way down to the lower
                    chambers where you find a plethora of gold and jewels as well as a few silver weapons. After packing up all the treasure you head back up
                    only to find a large cloud of smoke in the sky a few miles away from you in the direction of the town. You wonder if you made the right 
                    decision. The only thing necessary for the triumph of evil is for good men to do nothing.
                    """)
                    adventureResult("evil end")

            #Player chose to get himself a slightly dangerous job as a bodyguard
            else:
                print("""
                Life had it's ups and downs for you, like most jobs you have good days and you have bad days. Only problem is that being a bodyguard makes
                the bad days alot more painful, but all in all you come out alive into an early retirement and unfortunately no adventurous life. You 
                spend most days trading stories with other retired bodyguards in the area and attending parties because of the connections you made 
                in your life.
                """)
                gameOver()


menu()
        