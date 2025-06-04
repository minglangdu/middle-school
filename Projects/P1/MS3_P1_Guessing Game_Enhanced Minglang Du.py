"""
Enhancement ideas:
* difficulty level giving fewer guesses and having closer bomb distance
* in the result list, log the difficulty and reasons
* have a time limit
"""


from random import *
from time import *

def gmsg(dist): # function to get message for each distance
    if (dist <= 5):
        return "Your guess is very close (within 5) "
    elif (dist <= 10):
        return "Your guess is close (6 to 10 away) "
    elif (dist <= 30):
        return "Your guess is somewhat close (11 to 30 away) "
    elif (dist <= 50):
        return "Your guess is neither close nor far (31 to 50 away) "
    elif (dist <= 70):
        return "Your guess is far (51 to 70 away) "
    else:
        return "Your guess is very far (71 to 100 away) "

print("""
Welcome to the Number Guessing Game!
In this game, you will try to guess a target number between 1 and 100.
But be careful! There's also a bomb number hidden close to the target.
If you guess the target number, you win!
But if you guess the bomb number or use up all your tries without guessing the target, you lose.
Let's start the game!
""")
results = [] # result list
game = 1
while 1: # means game will continue unless broken.
    diff = -1
    while 1: # ensures difficulty is between 1 and 5
        try: # if the difficulty entered is not an int, it will catch the error. 
            diff = int(input("Enter a difficulty between 1 and 5, with 5 being the highest: "))
            if diff <= 0 or diff > 5:
                raise KeyboardInterrupt() # trigger the try except when invalid input
            break # only runs if try except hasn't been triggered. 
        except:
            pass
    variation = 5 * (6 - diff) # changes possible bomb distance based on difficulty
    guesses = 10 + (3 - diff) # changes guesses based on difficulty
    ans = randint(1, 100) 
    bomb = ans
    while bomb == ans: # loops on and on until bomb is not ans but between 1 and 100
        bomb = randint(max(ans - variation, 0), min(100, ans + variation))
    # pick allotted time    
    secs = -1
    while 1:
        try: # if the time is not an int, it will catch the error
            secs = int(input("Enter a time limit in seconds (recommended 15 to 30): "))
            break # only goes out if valid answer
        except:
            print("Invalid.")
    start = time() # take the start time
    while 1: # similar to above while loop
        if (time() - start > secs): # check if elapsed time is over secs. 
            results.append("Game " + str(game) + ": Loss (Difficulty " + str(diff) + ") No time")
            print("Sorry, you didn't find the target in your given time. You lose.")
            break
        # check if there are no guesses
        if (guesses <= 0):
            results.append("Game " + str(game) + ": Loss (Difficulty " + str(diff) + ") No guesses")
            print("Sorry, you didn't find the target in your given guesses. You lose.")
            break
            
        print("You have " + str(guesses) + " guesses left.\n")
        guess = ""
        # checks if guess is a number and between 1 and 100
        while not (guess.isdecimal() and int(guess) > 0 and int(guess) <= 100):  
            guess = input("Please guess a number between 1 and 100: ")
            print()
        # checks validity
        guess = int(guess)
        if (guess == bomb):
            results.append("Game " + str(game) + ": Loss (Difficulty " + str(diff) + ") Hit bomb")
            print("Sorry, you hit the bomb. You lose.")
            break
        if (guess == ans):
            results.append("Game " + str(game) + ": Win (Difficulty " + str(diff) + ") Guessed correctly")
            print("You found the target! You win!")
            break
        # says guess nearness
        adist = abs(guess - ans)
        bdist = abs(guess - bomb)
        print(gmsg(adist) + "to the target.")
        print(gmsg(bdist) + "to the bomb.\n")
        # decrement guesses
        guesses -= 1
    
    game += 1
    # print results
    print("Target number was:", ans)
    print("Bomb number was:", bomb)
    print()
    for i in results:
        print(i)
    # check if player wants to continue
    print()
    if (input("Would you like to play again? (y/n)").lower() != "y"):
        break
    print()