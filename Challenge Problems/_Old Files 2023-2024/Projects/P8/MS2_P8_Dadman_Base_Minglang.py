import random
import sys
import time

# a list of the many words you have to guess
phrases = [
    ["Fear", ["spiders", 'five five five five five', 'shoggoth', 'capitalism',
              'debt', 'corruption', 'more debt', 'diseases', 'triangle', 'non-cube']],
    ["The Unknown", ["test grades", "negativity", "the starfish", "library of babel",
                     "inordinate", "square pegs in round holes", "incompetence", "disgusting",
                     "pyramid"]]
]

# introduce the user to the game
print("""
___________________________________________________________________________ 

Welcome to the Dadman Game!

This game is similar to hangman but without all the
gratuitous hanging. Instead, you are in an even scarier
situation. You did Something Very Bad and have been sent
to your room. Your dad is slowly making his way up the
stairs to give you a Talk. You are trying to come up with
a good explanation for why you did the thing you did
before your dad makes it to the top of the stairs.

Because this is a game, the only way to come up with such
an excuse is to first solve a word puzzle, and quickly.
Solve away...
___________________________________________________________________________ 
""")
def start(): # start a new session
    # print puzzle categories.
    print("Please select one of the following puzzle categories:\n")
    i = 1
    for name in phrases:
        print(str(i) + ". " + name[0])
        i += 1

    word = "" # define guess word
    while word == "":
        try: # check for bad answers
            choice = int(input()) - 1 # ask user
            word = random.choice(phrases[choice][1])
        except:
            print("Invalid decision. Try again!")

    dadstat = 6 # guesses left
    dad = [ # a narration that keeps the player engaged
    """The silence in your room is broken by the thunderous \
    pound of a boot, a sound that threatens to overwhelm your \
    very consciousness. Knowing you only have some time to appeal \
    to this dread entity, you yell out letters into the void. """,
    """
    The first wrong answer of many. A faster movement is the \
    only answer it gives you.
    """,
    """
    Again, you give an incorrect answer. It is at your stairs, piercing \
    the darkness with its glowing eyes.
    """,
    """
    You have already gotten three strikes, but aren't out yet. IT has gotten \
    to the top step of the stairs. It won't be long before it finds you.
    """,
    """
    Once again, you get it wrong. It has been slowed by the unstable barricade \
    at your door, giving you some time.
    """,
    """
    It is searching the room with its knowing eyes. It would take only one \
    wrong answer to give away your location.
    """,
    """
    Though your eyes are closed, you know it in your bones that you \
    have failed. The darkness consumes you, omnipresent and immortal, \
    an antithesis to all that is good.
    """]
    guesses = [] # list of guessed letters
    correct = False # correct guess -> don't repeat flavor text.
    while True:
        # print flavor text
        if not correct:
            print(dad[6 - dadstat], end="\n\n" + "*" * 10 + "\n\n")
        correct = False
        print("Guesses:", *guesses) # show guessed letters
        won = True # check if won
        for i in word:
            if i in guesses: # guessed -> revealed
                print(i, end=" ")
            elif i.isalpha(): # not guessed and not symbol
                print("_", end=" ")
                won = False # unrevealed -> not won
            else: # symbols and spaces are left as is
                print(i, end=" ")
        print()
        
        # game over states
        if dadstat <= 0: # lose state
            print("Correct answer:", word)
            break
        if won: # win state
            print("Congratulations! You have won... for now.")
            break
        
        flag = False # flag means valid guess
        while flag == False:
            print(str(dadstat), file = sys.stderr, end="")
            print(" guesses left.") # show chances left
            choice = input() # get user choice
            if (len(choice) != 1 or not choice.isalpha() or choice in guesses): # invalid guess
                print("No, you tell yourself. That is not the right answer. You don't have much time before", end="")
                print(" it ", file=sys.stderr, end = "")
                print("finds you.","*" * 10,sep="\n")
            else:
                flag = True # valid guess
                guesses.append(choice) # add to guesses
                if (choice in word):
                    # indicate correctness
                    correct = True
                    print("You feel like you said the right letter.\n\n" + "*" * 10 + "\n\n")
                else:
                    dadstat -= 1
            
start()