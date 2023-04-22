import sys

endings = {"good end" : 0, "evil end" : 0, "died" : 0, "secret end" : 0}

def menu():
    choice = 0
    while choice < 1 or choice > 4:
        print("""
        1. Text Adventure
        2. Dice
        3. Rock Paper Scissor
        4. Exit
        """)
        try:
            choice = int(input("Enter your selection: "))
            match choice:
                case 1:
                    #function, remove break
                    break
                case 2:
                    #function, remove break
                    break
                case 3:
                    #function, remove break
                    break
                case 4:
                    sys.exit("Goodbye.")
                case _:
                    print("Please make a valid selection")
        except ValueError:
            print("Please enter a number.")

def yesOrNo():
    while True:
        choice = input("Please enter y for yes or n for no")
        if choice.lower is "y" or "n":
            return choice
        print("Invalid input, try again")
        

def selectPath():
    while True:
        try:
            choice = int(input("To select the first option enter 1, to select the second option enter 2. Choose wisely"))
            match choice:
                case 1, 2:
                    return choice
                case _:
                    print("Please make a valid selection")
        except ValueError:
            print("Please enter an integer")

def gameOver():
    print("Game over, press enter to return to menu")
    input()
    menu()

def printEndings():
    for ends, amounts in endings:
        print(ends, amounts, end=" ")

def adventureResult(end):
    if end in endings:
        endings[end] += 1
    else:
        print("Congratulations you found a secret end")
        endings["secret end"] += 1

def selectPath():
    print("""
        Heroes distinguish themselves through their primary attribute, namely: Strength, Intelligence and Charisma.
        What do you covet young adventurer? The decisions you make will alter the destiny that awaits you.
        (Please enter strength, intelligence or charisma to begin your adventure)
        """)
    while True:
        pathSelection = input()
        match pathSelection.lower:
            case "strength":
                strengthPath()
            case "intelligence":
                break
            case "charisma":
                break
            case _:
                print("Please check your spelling or make a valid selection.")

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
            else:
                print("""
                You work your way up the stairs, surprinsingly nimble for a person of you size. The third door on your left you notice
                is slightly ajar. Inside you find the king of the country lying in a pool of his own blood, standing over him a shadowy
                figure wielding glistening metal. Before your brain can finish processing the scene the figure sees you and escapes out
                the window. Your first instict is to chase down the assassin, but your eyes find the illegal things in the room. You
                could chase down the assassin or you could instead clean up after the king and report this to the council.
                """)
                choiceUpstairs = selectPath()
                if choiceUpstairs == 1:
                    print("""
                    You were good up until the very end, you feel the cold, hard ground underneath your face. Confused as to what exactly
                    happened. Honestly so am I, those guys were crazy fast. At least I think it was more than one.
                    """)
                    gameOver()
                else:
                    print("""
                    Not your most honest work, definitely. Regardless, the council thanked you very much for your discretion. So much
                    that you are now minor nobility, given some land to west for your silence in this embarrasing incident. Maybe not
                    the adventure you wanted but its a nice ending, kinda.
                    """)
                    adventureResult("win?")
        else:
            print("""
            You lean over and pick the relatively light sack, the smaller one looks up to you with a half disinterested smile. 
            "Thank you, this way" you realize after your new companion spoke that she sounds much older. Its hard to tell age
            underneath all that cloth and wizards hat. You spend most of your day fetching books and hauling them around. You 
            feel it has been mostly wasted, boredom even drove you to glance at some of the wizards books. She seems very pleased
            with your help and offers you to apprentice under her as a novice mage. Would you like to accept her offer or maybe
            get in a party wasn't the best idea after all and you feel like you would rather try your luck outside on your own?
            """)
            choiceBooks = selectPath()
            if choiceBooks == 1:
                print("""
                
                """)
            else:
                print("""
                
                """)
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



        