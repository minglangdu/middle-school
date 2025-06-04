"""
Arcade/Adventure Currency Simulator
"""

# Importing modules.
import random # Random is used to calculate random events.
import time # Time is used to put time between prompts (e.g. rock paper scissors).
import math # Math is used to useful math functions needed (e.g. floor).

# Define variables
wallet = 10000 # The amount of money you currently have.
rps = ['rock', 'paper', 'scissors'] # Used for rock paper scissors
flip = ['heads', 'tails'] # Used for coinflip
hl = ['higher', 'lower', 'jackpot'] # Used for highlow
coin_multi = 1 # Coin multiplier
# Element 1 is rps, element 2 is highlow, element 3 is coinflip, element 4 is guessing game, and element 5 is adventure.
wins = [0, 0, 0, 0, 0] # Wins
losses = [0, 0, 0, 0, 0] # Losses
draws = [0, 0, 0, 0, 0] # Draws (or other stats)
cheats = 5 # The amount of available cheats
level = 0 # The level you are currently on
exp = 0 # Experience needed to level up
exp_multi = 1 # Experience multiplier
title = "" # Title
achievements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # Achievements
shop_bought = [0, 0, 0, 0] # Used for the shop. 1st element is coin multiplier, 2nd element is experience multiplier, 3rd element is experience, and 4th element is levels.
adv_interaction = 0 # Used to count the interactions in an adventure.
adv_money = 0 # Used to store the money you earned in an adventure.
current_adv = 0 # Used to store the name of the adventure you are currently doing.
interactions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Used to keep track of adventure interactions.
mil_coins = False # Used to determine if one has gotten "Millionare" title yet.

def free_money():
    """
    This is a cheat code that when used, gives you free money (multiplied by your experience multiplier).
    """
    # Calling global variables.
    global coin_multi
    # Informs the user that they have used a cheat code.
    print("! Cheat code: Free Money Activated ! ")
    # Generating the amount of money given.
    moolah = random.randint(100, 1000)*coin_multi
    # Informs the user about how much money they receive.
    print("You get " + str(moolah) + "!")
    # When the function returns, the return value will be added to their current balance.
    return moolah

def free_level():
    """
    This is a cheat code used to give the user a free level.
    """
    # Calling global variables.
    global level
    # Informs the user that they have leveled up.
    print("! Cheat code: Free Level Activated ! ")
    # Increases the level.
    level += 1
    # Calls a function to check if they have gotten any rewards for leveling up (scroll down for the function).
    check_level(level)

def free_exp():
    """
    This is a cheat code that gives the user 10 experience points multiplied by their experience multiplier.
    """
    # Calling global variables.
    global exp_multi, exp
    # Informs the user that they activated the cheat code.
    print("! Cheat code: Free Experience Activated ! ")
    # Calculates the gained experience.
    gain = 10*exp_multi
    # Informs the user that they have gained experience.
    print("You gained " + str(gain) + " EXP!")
    # The returned value will be added to the user's current experience.
    return gain

def cheat_code(val):
    """
    This is a function used to call the cheat codes that the user has entered. (Enhancement)
    For the parameter val: 1 is for free money, 2 is for free level, and 3 is for free experience.
    This function also checks if the user has enough cheats left to use.
    There are default 5 cheats, and more can be obtained through leveling.
    """
    # Calling global variables.
    global wallet, cheats, exp
    # Checks if the user has no cheats left. If so, inform the user and exit the function.
    if cheats == 0:
        print("You have no cheats left. You are unable to use any more cheats.")
        return 0;
    # Decrease the amount of available cheats by 1.
    cheats -= 1
    # These statements check for which helper function should be called.
    if val == 1:
        wallet += free_money()
    if val == 2:
        free_level()
    if val == 3:
        exp += free_exp()

def rock_paper_scissors():
    """
    This function is used to play the rock-paper-scissors game.
    First, "Rock, Paper, Scissors, Shoot!" is printed.
    Then, the user is inputted for his/her move.
    An move is generated for the AI.
    Rock beats scissors, scissors beats paper, and paper beats rock.
    If the user wins the game, the user wins money.
    If the game is drawn, no money is won/lost.
    Otherwise, the user loses money.
    """
    # Calling global variables.
    global wallet, exp, exp_multi
    # The beginning of a rock paper scissors game.
    print("Rock, ")
    time.sleep(1)
    print("Paper, ")
    time.sleep(1)
    print("Scissors, ")
    time.sleep(1)
    print("Shoot!")
    # Get the move from the player.
    player_move = input("What do you choose? ('rock', 'paper', or 'scissors') ")
    # If invalid, exit the function.
    if player_move not in rps:
        print("Invalid move.")
        return 0;
    # Determines the computer's move (it's random).
    ai_chance = random.randint(1, 3)
    ai_move = rps[ai_chance - 1]
    # Informs the user about which handsigns are chosen.
    print("You chose " + player_move + ", and the computer chose " + ai_move + ".")
    # These statements check if one wins, draws, or loses.
    if player_move == ai_move:
        # If both handsigns are the same, the game is drawn.
        print("The game is drawn. You win nothing.")
        draws[0] += 1
    elif (player_move == "rock" and ai_chance == 2) or (player_move == "paper" and ai_chance == 3) or (player_move == "scissors" and ai_chance == 1):
        # If the player fails the conditions mentioned in the header of the function, they lose the game.
        lost_amt = math.floor(random.randint(500, 1500)*coin_multi)
        print("You lost the game! You lost " + str(lost_amt) + ".")
        wallet -= lost_amt
        losses[0] += 1
    else:
        # Otherwise, the player wins.
        won_amt = math.floor(random.randint(500, 1500)*coin_multi)
        print("You win the game! You win " + str(won_amt) + ".")
        wallet += won_amt
        wins[0] += 1
        exp += exp_multi
        
def highlow():
    """
    This is a game of highlow.
    Two random numbers between 1 and 100 will be generated: one for the given, and one for the secret.
    The user will be prompted if the number is higher, lower, or the same (jackpot) as the secret number.
    If the user gets it right, they will win coins. Jackpot wins big!
    Otherwise, the user loses.
    """
    # Initiating global variables.
    global wallet, wins, losses, exp, exp_multi
    # Generate the secret and given numbers.
    secret = random.randint(1, 100)
    given = random.randint(1, 100)
    # Prompts the user to choose an option.
    x = input("Is the secret number higher or lower than " + str(given) + "? (Options are 'higher', 'lower', and 'jackpot'.) ")
    # If invalid, exits the function.
    if x not in hl:
        print("Invalid input.")
        return 0;
    # Informs the user about the numbers.
    print("The given number was " + str(given) + " and the secret number was " + str(secret) + ".")
    # Checks if the user wins the game.
    if (secret > given and x == "higher") or (secret < given and x == "lower"):
        # If so, print the win message, and reward the user coins.
        value = math.floor(random.randint(500, 1500)*coin_multi)
        print("You win " + str(value) + "!")
        wallet += value
        wins[1] += 1
        exp += exp_multi
    # Otherwise, check if the user lost the game.
    elif (secret > given and x != "higher") or (secret < given and x != "lower") or (secret == given and x != "jackpot"):
        # If so, prints the loss message and subtracts some coins.
        value = math.floor(random.randint(500, 1500)*coin_multi)
        print("You lost " + str(value) + "!")
        wallet -= value
        losses[1] += 1
    # Checks if the user got the jackpot.
    elif secret == given and x == "jackpot":
        # If so, print the win message and reward the user a lot of coins.
        value = math.floor(random.randint(50000, 100000)*coin_multi)
        print("JACKPOT! You win " + str(value) + "!")
        wallet += value
        wins[1] += 1
        draws[1] += 1
        exp += 5*exp_multi
        
def statistics():
    """
    This function is used to display the statistics of the players (wins, losses, and draws/other conditions).
    Included are rock paper scissors, highlow, coinflip, guessing game, and adventure.
    """
    # Initiating variables.
    global wins, losses, draws
    # Prints the statistics.
    print("_________________________________________________")
    # Rock Paper Scissors: Wins, losses, and draws
    print("You have won " + str(wins[0]) + " rock paper scissors games, lost " + str(losses[0]) + " games, and drawn " + str(draws[0]) + " games.")
    # Highlow: wins, losses, and jackpots
    print("You have won " + str(wins[1]) + " highlow games, lost " + str(losses[1]) + " games, and won the jackpot in " + str(draws[1]) + " games.")
    # Coinflip: wins and losses
    print("You have won " + str(wins[2]) + " coinflip games and lost " + str(losses[2]) + " games.")
    # Guessing games: how many played
    print("You have played " + str(wins[3]) + " guessing games.")
    # Adventures: won aond lost
    print("You have won " + str(wins[4]) + " adventures and have lost " + str(losses[4]) + " adventures.")
    print("_________________________________________________")

def balance():
    """
    This function is used to print the user's profile.
    Included are the title, wallet, level, and current experience.
    """
    # Loading variables.
    global wallet
    # Prints the aforementioned points.
    print("_________________________________________________")
    # Checks if the user has a title.
    if title != "":
        # If so, print it out.
        print("Title: " + title)
    # How much the player has in his wallet.
    print("You have " + str(wallet) + " in your wallet.")
    # Which level the player is currently at.
    print("You are currently at level " + str(level) + ".")
    # How much experience needed to level up.
    print("Experience: " + str(exp) + "/100.")
    print("_________________________________________________")
    
def get_help():
    """
    This function is used to display help.
    After the commands are shown, the user is prompted if they want an in-depth explanation of a specific command.
    If so, an in-depth explanation will be printed.
    """
    # Prints the main help prompt
    print("""_________________________________________________
The commands are:
quit: exits the game
help: gets help
wallet: gives you a look of your wallet
statistics or stats: look at your win/loss/draw stats for certain games
rps or rock paper scissors: plays a game of rock paper scissors
highlow: play a game of highlow
coinflip: play a game of coinflip
adventure: starts an interactive adventure
shop: buy some permanent boosts with money
_________________________________________________""")
    # Prompts the user for an in-depth explanation.
    cmd = input("Do you want an in-depth explanation of what a command does? (Type in the name of the command.) ")
    # Help on the quit command.
    if cmd == "quit":
        return ("Simply quits the game.")
    # Help on the help command.
    elif "help" == cmd:
        return ("The command you are running right now.")
    # Help on the wallet/balance/profile commands.
    elif "wallet" == cmd or "balance" == cmd or "profile" in cmd:
        return ("""This command shows:
- Your title (if you have any)
- Your current level
- The amount of money you currently have
- Your experience you need to level up""")
    # Help on rock paper scissors.
    elif cmd == "rps" or cmd == "rock paper scissors":
        return ("""This is a rock paper scissors simulator.
First, "Rock, Paper, Scissors, Shoot!" will appear on the screen.
Next, you will be prompted which handsign you will choose.
Rock, Paper, and Scissors are the valid inputs.
A handsign will be randomly generated for the computer.
You win if you follow the rules:
rock beats scissors, paper beats rock, and scissors beats paper.
If the handsigns are the same, the game is drawn.
Otherwise, you lose the game.""")
    # Help on statistics.
    elif cmd == "statistics" or cmd =="stats":
        return ("This command shows your statistics in the minigames you have played (wins, losses, draws/other stuff)")
    # Help on highlow.
    elif cmd == "highlow":
        return ("""This is a game of highlow.
A random number is generated for the given, and another is generated for the secret.
You will have to guess if the number is higher, lower, or the same (jackpot) as the secret number.
If you guess right, you win! Jackpot wins big. Otherwise, you lose.""")
    # Help on coinflip.
    elif cmd == "coinflip":
        return ("""This game is a simple coinflip simulator.
You will have to guess if the coin lands on heads or tails.
If you guess correctly, you win! Otherwise, you lose.""")
    # Help on the guessing game.
    elif cmd == "guess" or cmd == "guessing game":
        return ("""This is a guessing game simulator.
First, you will be prompted with a range that the secret number should be in. Don't make it too small, or it won't run.
Next, you will have to guess what the secret number is.
If you get it correct on your first try, good job! You will get a high coin payout.
If not, try again. You have unlimited tries for this game, but the more tries you take, your payout will be lower.
Also, the larger the range, the higher payout you get!""")
    # Help on adventrue.
    elif cmd == "adventure":
        return ("""This is an adventure simulator!
When you start an adventure, you will be prompted which adventure you want to do.
Once you select one, your adventure begins.
Each adventure consists of 10 interaction, 5 of which do nothing, and 5 of which you can interact with.
For the interactions you can interact with, there may be a random chance of you either winning coins, doing nothing, or losing everything you have earned and ending the adventure.
If you successfully make it out of the adventure, good job! You get to keep your rewards.""")
    # Help on the cheat codes.
    elif cmd == "money":
        return ("This is a cheat code! Run it to find out what it does.")
    elif cmd == "level":
        return ("This is a cheat code! Run it to find out what it does.")
    elif cmd == "experience":
        return ("This is a cheat code! Run it to find out what it does.")
    # Help on the shop.
    elif cmd == "shop":
        return ("This is a shop where you can buy multipliers (coin or experience), experience, or a level. Run the command for more detail on prices.")
    # If the user doesn't input something, exit the function.
    else:
        return ("Exiting.")

def coinflip():
    """
    This function is for the coinflip game.
    The user is prompted for a move, and the computer also generates a move (heads, tails).
    If both moves are the same, then the user wins.
    Otherwise, the user loses.
    """
    # Initiating variables.
    global wallet, wins, losses, exp, exp_multi
    # Prompts the user for a choice.
    x = input("Do you choose heads or tails? ('heads' or 'tails') ")
    # Checks if the input is valid; if not, exit the function.
    if x not in flip:
        print("Invalid input.")
        return 0
    # Generate the computer's move.
    ai_chance = random.randint(1, 2)
    ai_move = flip[ai_chance-1]
    # Informs the user about the choices.
    print("You chose " + x + ", and the result was " + ai_move + ".")
    # Checks if the moves are the same.
    if x == ai_move:
        # If so, print the win message, and reward the user with coins.
        value = math.floor(random.randint(500, 1500)*coin_multi)
        print("You win " + str(value) + "!")
        wallet += value
        wins[2] += 1
        exp += exp_multi
    else:
        # Otherwise, the user loses. The loss message is printed, and some coins are subtracted.
        value = math.floor(random.randint(500, 1500)*coin_multi)
        print("You lost " + str(value) + "!")
        wallet -= value
        losses[1] += 1
        
def guessing_game():
    # Initiate variables.
    global wallet, wins, exp, exp_multi
    # Gets an user input for the guessing range.
    range_min = int(input("What is your minimum range? "))
    range_max = int(input("What is your maximum range? "))
    tot_range = range_max - range_min
    # Checks if the maximum range is higher than minimum range. If it isn't, the user needs to run the program again.
    if tot_range < 5:
        print("The range is too small! Please run the program again.")
    # Otherwise, continue the program normally.
    else:
        # Generates the random number.
        x = random.randint(range_min, range_max)
        # Assigns variables to the number of guesses it takes and the current guess.
        guesses = 0
        guess = 0.1
        # This condition loops until the guess is correct.
        while guess != x:
            # Asks the user for a guess, and increase guess counter by one.
            guess = int(input("Guess a number: "))
            guesses += 1
            # Condition to check if the guess is correct.
            if int(guess) == x:
                print("Correct! You guessed it in " + str(guesses) + " guesses!")
                value = math.floor(random.randint(100, 300) * tot_range**(1/guesses))
                print("You won " + str(value) + "!")
                wallet += value
                wins[3] += 1
                exp += exp_multi*round(tot_range**(1/5))
                break
            # Otherwise, the guess is wrong.
            else:
                # Checks if the guess is smaller than the secret number, and tells the user that the secret number is higher than the guess.
                if guess < x:
                    print("The secret number is higher than " + str(guess) + ". Guess again.")
                # Otherwise, tells the user that the secret number is lower than the guess.
                else:
                    print("The secret number is lower than " + str(guess) + ". Guess again.")

def adv_result():
    """
    Prints the user's results in an adventure.
    Shown will be the adventure's name, the money found, and the interactions used.
    """
    # Initializing variables.
    global adv_interaction, adv_money, current_adv, wallet, wins, losses, interactions
    # Prints the results.
    print("______________________________________________")
    print("ADVENTURE RESULTS:")
    # Current adventure
    print("Adventure: " + current_adv)
    # Money found on the adventure
    print("You found " + str(adv_money) + " on your " + current_adv + " adventure.")
    # Interactions in the adventure
    print("Interactions: " + str(adv_interaction))
    # Adds the amount of money to the wallet
    wallet += adv_money
    # Checks if there are still interactions left; if so, add to losses; else, add to wins
    if interactions != []:
        losses[4] += 1
    else:
        wins[4] += 1
    # Resets both stats to 0
    adv_interaction = 0
    adv_money = 0

def adventure():
    """
    This lengthy function is for adventure.
    There are two adventures: Jungle Quest and Ship Travels.
    Both have 10 interactions, 5 which are interactive and 5 that do nothing.
    For the 5 interactive interactions, a user will be prompted with 2 choices.
    Both choices may have a chance to win coins and a chance to die (lose everything and end adventure).
    Once the user dies/reaches 10 interactions, the adventure ends.
    """
    # Initiating variables.
    global adv_interaction, adv_money, current_adv, interactions, wins, exp, exp_multi
    # Checks if the user isn't currenty in an adventure.
    if adv_interaction == 0:
        # If so, prompt the user which one they want to choose.
        x = input("What adventure do you want to choose? ('Jungle Quest' or 'Ship Travels') ").lower()
        if x == 'jungle quest':
            # First adventure, Jungle Quest
            print("Starting the adventure Jungle Quest!")
            current_adv = 'Jungle Quest'
            adv_interaction += 1
            interactions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        elif x == 'ship travels':
            # Second adventure, Ship Travels
            print("Starting the adventure Ship Travels!")
            current_adv = 'Ship Travels'
            adv_interaction += 1
            interactions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        else:
            # If the name isn't valid, the function is exitied.
            print("Invalid adventure name.")
    # Checks if the user has used up all the interactions.
    elif interactions == []:
        # If so, the adventure ends, and the user keeps everything found.
        print("You have reached the end of your adventure, congrats!")
        exp += 10*exp_multi
        adv_result()
    # Otherwise, the interactions are displayed.
    else:
        # Increments the adventure interaction by 1.
        adv_interaction += 1
        # Checks if current advetnure is the Jungle Quest.
        if current_adv == 'Jungle Quest':
            # If so, a random interaction is chosen.
            x = random.choice(interactions)
            # Interaction check.
            if x == 1:
                # First interaction, treasure chest, interactive
                interactions.remove(1)
                y = input("You come across a treasure chest in the jungle. What do you choose? ('Open it' or 'Run away') ").lower()
                if y == 'open it':
                    # Choice 1: high chance for a moderate amount of coins, or nothing/death
                    chance = random.randint(1, 4)
                    if chance == 1:
                        print("It was a booby trap! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                    elif chance == 2:
                        print("It was a booby trap! You escape but with nothing. (nothing interesting happened)")
                    else:
                        asdf = random.randint(1000, 5000)
                        print("You found " + str(asdf) + " inside the treasure chest!")
                        adv_money += asdf
                elif y == 'run away':
                    # Choice 2: does nothing
                    print("You run away from the treasure chest. (nothing interesting happened)")
                else:
                    print("Invalid input. (nothing interesting happened)")
            elif x == 2:
                # 2nd interaction: stray cat, interactive
                interactions.remove(2)
                x = input("You find a stray cat in the jungle. What do you do? ('keep it' or 'run away') ").lower()
                if x == 'keep it':
                    # Choice 1: chance of a moderate amount of coins, high chance of nothing, and chance of death
                    chance = random.randint(1, 5)
                    if chance == 1:
                        print("The cat was sick, and you got sick! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(2)
                        adv_result()
                    elif chance == 2 or chance == 3:
                        print("Before you could grab it, the cat ran away. (nothing interesting happened)")
                    else:
                        asdf = random.randint(2000, 3000)
                        print("You get hold of the cat and bring it to a pet shelter. As a reward, you were rewarded " + str(asdf) + ".")
                        adv_money += asdf
                elif x == 'run away':
                    # Choice 2: always does nothing
                    print("You successfully ran away from the cat. (nothing interesting happened)")
                else:
                    print("Invalid input. (nothing interesting happened)")
            elif x == 3:
                # Third interaction, gets lost in jungle, interactive
                interactions.remove(3)
                x = input("You got lost in the jungle! What do you do? ('try to escape' or 'stay') ").lower()
                if x == 'try to escape':
                    # Option 1: chance of high amount of coins, death, or nothing happens
                    chance = random.randint(1, 3)
                    if chance == 1:
                        asdf = random.randint(5000, 10000)
                        print("You made it out! You tell your story and gain " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("You made it out, but earned nothing. (nothing interesting happened)")
                    else:
                        print("You couldn't find your way out. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'stay':
                    # Option 2: chance of very high amount of coins, high chance of death, or nothing happens.
                    chance = random.randint(1, 4)
                    if chance == 1:
                        asdf = random.randint(10000, 20000)
                        print("You stayed in one place, and you were saved! As a reward, you were given " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("You stayed in one place but help did not come. You ended up escaping, but with nothing. (Nothing interesting happened)")
                    else:
                        print("You weren't able to find any help. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 4:
                # Interaction 4: River, interactive
                interactions.remove(4)
                x = input("You find a river. What do you do? ('go across' or 'go back') ").lower()
                if x == 'go across':
                    # Choice 1: chance of a high amount of coins, nothing, or death.
                    chance = random.randint(1, 3)
                    if chance == 1:
                        asdf = random.randint(5000, 10000)
                        print("You took a swim in the river and found " + str(asdf) + " lying around.")
                        adv_money += asdf
                    elif chance == 2:
                        print("You made it to the other side of the river, but with nothing. (nothing interesting happened)")
                    else:
                        print("You went into the river but couldn't find your way out. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'go back':
                    # Choice 2: nothing
                    print("You retreated away from the river. (Nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 5:
                # Interaction 5: Camping ground, interactive
                interactions.remove(5)
                x = input("You see a camping ground. What do you do? ('Approach' or 'Flee') ").lower()
                if x == 'approach':
                    # Choice 1: Chance of very high amount of coins, nothing happens, or high chance of death.
                    chance = random.randint(1, 4)
                    if chance == 1:
                        asdf = random.randint(10000, 20000)
                        print("You were welcomed at the camping site and was rewarded " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("The campers didn't want you near them and sent you out. (nothing interesting happened)")
                    else:
                        print("It was a booby trap! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'flee':
                    # Choice 2: does nothing
                    print("You fled from the campsite. (Nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 6:
                # Interaction 6: Does nothing
                interactions.remove(6)
                print("Nothing to see around but many, many trees. (nothing interesting happened)")
            elif x == 7:
                # Interaction 7: Does nothing
                interactions.remove(7)
                print("You found yourself retracing your steps. (nothing interesting happened)")
            elif x == 8:
                # Interaction 8: Does nothing
                interactions.remove(8)
                print("Being very tired, you fell asleep. (nothing interesting happened)")
            elif x == 9:
                # Interaction 9: Does nothing, also kind of an easter egg
                interactions.remove(9)
                print("You come across many gophers! Oh well, time to leave. (nothing interesting happened)")
            elif x == 10:
                # Interaction 10: Does nothing
                interactions.remove(10)
                print("You come across a super tall tree. You take a picture of it. (nothing interesting happened)")
        elif current_adv == "Ship Travels":
            # Second adventure, Ship Travels
            x = random.choice(interactions)
            if x == 1:
                # First Interaction: Deserted island, Interactive
                interactions.remove(1)
                x = input("You see a deserted island. What do you do? ('Search it' or 'Flee') ").lower()
                if x == 'search it':
                    # Choice 1: Chance of high amoount of coins, nothing, or death
                    chance = random.randint(1, 3)
                    if chance == 1:
                        asdf = random.randint(5000, 10000)
                        print("You go on the island and find " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("There was nothing on the island. (nothing interesting happened)")
                    else:
                        print("There were dangerous animals on the island! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'flee':
                    # Choice 2: Does nothing
                    print("You ignored the island. (Nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 2:
                # Second interaction: Storm, interactive
                interactions.remove(2)
                x = input("You see a storm in the distance! What do you do? ('Sail through' or 'Turn back') ").lower()
                if x == 'sail through':
                    # Choice 1: Chance for a very high amount of coins, nothing, or a high chance of death
                    chance = random.randint(1, 4)
                    if chance == 1:
                        asdf = random.randint(10000, 20000)
                        print("You successfully sailed through the storm! You tell your adventures and gain " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("The storm was too extreme, and you were forced to turn back. (nothing interesting happened)")
                    else:
                        print("You didn't make it through the storm. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'turn back':
                    # Choice 2: nothing happens
                    print("You avoided the storm. (Nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 3:
                # Interaction 3: Ship runs out of fuel
                interactions.remove(3)
                x = input("Your ship ran out of fuel! What do you do? ('Search for fuel' or 'Abandon ship') ").lower()
                if x == 'search for fuel':
                    # Choice 1: High chance of a moderate amount of coins or death
                    chance = random.randint(1, 4)
                    if chance < 4:
                        asdf = random.randint(2500, 5000)
                        print("You searched the ship and found fuel! While searching, you also found " + str(asdf) + ".")
                        adv_money += asdf
                    else:
                        print("You didn't find any fuel. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'abandon ship':
                    # Choice 2: Chance for a very very high amount of coins, and a very high chance of death
                    chance = random.randint(1, 5)
                    if chance == 1:
                        asdf = random.randint(10000, 50000)
                        print("You abandoned ship, but was rescued by another ship! As a reward, you were given " + str(asdf) + ".")
                        adv_money += asdf
                    else:
                        print("How silly of you to do that. You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 4:
                # Interaction 4: Another ship, interactive
                interactions.remove(4)
                x = input("You see another ship in the distance. What do you do? ('Contact the ship' or 'Sail by') ").lower()
                if x == 'contact the ship':
                    # Choice 1: Chance of a moderate amount of coins, nothing happens, or death
                    chance = random.randint(1, 4)
                    if chance < 3:
                        asdf = random.randint(2500, 5000)
                        print("You connected with the ship and the other ship's captain gave you " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 3:
                        print("The captain of the other ship didn't want any visitors. (nothing interesting happened)")
                    else:
                        print("It was a pirate ship! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'sail by':
                    # Choice 2: nothing happens
                    print("You ignore the other ship. (nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 5:
                # 5th interaction: pirate ship, interactive
                interactions.remove(5)
                x = input("You see a pirate ship in the distance. What do you do? ('Fight' or 'Flee') ").lower()
                if x == 'fight':
                    # Choice 1: Chance of a high amount of coins, nothing happens, or die
                    chance = random.randint(1, 3)
                    if chance == 1:
                        asdf = random.randint(5000, 10000)
                        print("You won the battle and received " + str(asdf) + ".")
                        adv_money += asdf
                    elif chance == 2:
                        print("No one won the battle. (nothing interesting happened)")
                    else:
                        print("You lost the battle! You lost everything and your adventure has ended.")
                        adv_money = 0
                        interactions.append(1)
                        adv_result()
                elif x == 'flee':
                    # Second choice: Does nothing
                    print("You fled from the pirate ship. (nothing interesting happened)")
                else:
                    print("Invalid command (nothing interesting happened).")
            elif x == 6:
                # Interaction 6: Sharks, not interactive
                interactions.remove(6)
                print("You see a group of sharks in the distance. (nothing interesting happened)")
            elif x == 7:
                # Interaction 7: Mountains, not interactive
                interactions.remove(7)
                print("You spot some mountains in the distance. Oh well, time to head back to the open ocean. (nothing interesting happened)")
            elif x == 8:
                # Interaction 8: Fleet of ships, not interactive
                interactions.remove(8)
                print("You see a fleet of ships in the distance. Better stay far away from them. (nothing interesting happened)")
            elif x == 9:
                # Interaction 9: Water, not interactive
                interactions.remove(9)
                print("You take a look around, and the only thing you see is water, as far as the eye can see. (nothing interesting happened)")
            elif x == 10:
                # Interaction 10: Boredom, not interactive
                interactions.remove(10)
                print("You got bored, so you decided to read a book. (nothing interesting happened)")

def check_level(lvl):
    """
    This function is used to inform the user that they have leveled up and check for rewards. (enhancement)
    The highest level reward is level 100, where you will become a Level Master.
    """
    # Initiating variables.
    global exp_multi, wallet, cheats, coin_multi, title
    # Informs the user that they have leveled up.
    print("Level up! You are now at level " + str(lvl) + ".")
    # These following conditionals are used to check for rewards that users get at a certain level.
    if lvl == 1:
        print("As a reward, you got 10000 coins!")
        wallet += 10000
    elif lvl == 2:
        print("As a reward, you got a 2x EXP multiplier!")
        exp_multi *= 2
    elif lvl == 3:
        print("As a reward, you got 15000 coins!")
        wallet += 10000
    elif lvl == 4:
        print("As a reward, you got 20000 coins!")
        wallet += 20000
    elif lvl == 5:
        print("As a reward, you got a 2x coin multiplier!")
        coin_multi *= 2
    elif lvl == 10:
        print("As a reward, you got 25000 coins!")
        wallet += 25000
    elif lvl == 15:
        print("As a reward, you got 5 more cheats!")
        cheats += 5
    elif lvl == 20:
        print("As a reward, you got a 2x EXP multiplier!")
        exp_multi *= 2
    elif lvl == 25:
        print("As a reward, you got 30000 coins!")
        wallet += 30000
    elif lvl == 50:
        print("As a reward, you got a 2x coin multiplier!")
        coin_multi *= 2
    elif lvl == 75:
        print("As a reward, you got 50000 coins!")
        wallet += 50000
    elif lvl == 100:
        print("""As a reward, you got the following:
- 100000 coins
- 2x coin multiplier
- 2x EXP multiplier
- UNLIMITED cheats
- "Level Master" title""")
        wallet += 100000
        exp_multi *= 2
        coin_multi *= 2
        cheats = -1
        title = "Level Master"

def achs_check():
    """
    This function is used to check achievements. (enhancement)
    There are achievements for rock paper scissors, highlow, coinflip, guessing game, and adventure.
    For getting the achievement, the user will get rewards (e.g. coins, titles)
    """
    # Initiating Variables.
    global wallet, title, exp_multi, coin_multi
    # Achievements 1 and 2: Rock Paper Scissors
    if 1 in achievements:
        if wins[0] >= 10:
            print("New Achievement: Win 10 games of Rock Paper Scissors!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(1)
    if 2 in achievements:
        if wins[0] >= 100:
            print("New Achievement: Win 100 games of Rock Paper Scissors!")
            print("Rewards: 100000 coins, 'RPS Master' title")
            wallet += 100000
            title = "RPS Master"
            achievements.remove(2)
    # Achievement 3 and 4: Highlow
    if 3 in achievements:
        if wins[1] >= 10:
            print("New Achievement: Win 10 games of Highlow!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(3)
    if 4 in achievements:
        if wins[1] >= 100:
            print("New Achievement: Win 100 games of Highlow!")
            print("Rewards: 100000 coins, 'Highlow Master' title")
            wallet += 100000
            title = "Highlow Master"
            achievements.remove(4)
    # Achievement 5 and 6: Coinflip
    if 5 in achievements:
        if wins[2] >= 10:
            print("New Achievement: Win 10 games of Coinflip!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(5)
    if 6 in achievements:
        if wins[2] >= 100:
            print("New Achievement: Win 100 games of Coinflip!")
            print("Rewards: 100000 coins, 'Coinflip Master' title")
            wallet += 100000
            title = "Coinflip Master"
            achievements.remove(6)
    # Achievement 7 and 8: Guessing Game
    if 7 in achievements:
        if wins[3] >= 10:
            print("New Achievement: Win 10 Guessing Games!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(7)
    if 8 in achievements:
        if wins[3] >= 100:
            print("New Achievement: Win 100 Guessing Games!")
            print("Rewards: 100000 coins, 'Guessing Game Master' title")
            wallet += 100000
            title = "Guessing Game Master"
            achievements.remove(8)
    # Achievement 9 and 10: Adventure
    if 9 in achievements:
        if wins[4] >= 5:
            print("New Achievement: Win 5 adventures!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(9)
    if 10 in achievements:
        if wins[4] >= 25:
            print("New Achievement: Win 25 adventures")
            print("Rewards: 100000 coins, 'Adventure Master' title")
            wallet += 100000
            title = "Adventure Master"
            achievements.remove(10)
    # Achievement 11 and 12: Jackpots in Highlow
    if 11 in achievements:
        if draws[1] == 1:
            print("New Achievement: Win a jackpot!")
            print("Reward: 10000 coins")
            wallet += 10000
            achievements.remove(11)
    if 12 in achievements:
        if wins[4] >= 25:
            print("New Achievement: Win 5 jackpots!")
            print("Rewards: 100000 coins, 'Master of Luck' title")
            wallet += 100000
            title = "Master of Luck"
            achievements.remove(12)
    # Last Achievement: Obtain every other achievement
    if achievements == []:
        print("New Achievement: Obtain All Other Achievements!")
        print("Rewards: 500000 coins, 2x EXP multiplier, 2x coin multiplier, 'Achievement Master' title")
        wallet += 500000
        exp_multi *= 2
        coin_multi *= 2
        title = "Achievement Master"
        achievements.append("Finished")

def shop():
    """
    This is a shop, where you can buy some perks to improve your gameplay with in-game currency. (enhancement)
    More information in the print statement below.
    """
    # Initiate variables.
    global shop_bought, coin_multi, wallet, exp_multi, exp, level
    # Informs the user about the shop's quantity.
    print("""What do you want to buy? The options are:
1. 2x coin multiplier, cost: 10000 (exponentially increases as you buy more)
2. 2x EXP multiplier, cost: 10000 (exponentially increases as you buy more)
3. 10 experience points (multiplied by your EXP multi), cost: 5000
4. +1 level, cost: 20000
Type in the number of the product you want to buy.""")
    try:
        x = int(input())
    except ValueError:
        print("Invalid input.")
        return 0
    # Item 1: 2x coin multiplier
    if x == 1:
        cost = 10000*(2**shop_bought[0])
        if wallet < cost:
            print("You don't have enough coins to pay the fee: " + str(cost))
        else:
            shop_bought[0] += 1
            wallet -= cost
            print("Bought 2x coin multiplier!")
            coin_multi *= 2
    # Item 2: 2x experience multiplier
    elif x == 2:
        cost = 10000*(2**shop_bought[1])
        if wallet < cost:
            print("You don't have enough coins to pay the fee: " + str(cost))
        else:
            shop_bought[1] += 1
            wallet -= cost
            print("Bought 2x EXP multiplier!")
            exp_multi *= 2
    # Item 3: 10 experience points (multiplied by your experience multiplier)
    elif x == 3:
        cost = 5000
        if wallet < cost:
            print("You don't have enough coins to pay the fee: " + str(cost))
        else:
            shop_bought[2] += 1
            wallet -= cost
            print("Bought 10 experience points!")
            exp += 10*exp_multi
    # Item 4: One level
    elif x == 4:
        cost = 20000
        if wallet < cost:
            print("You don't have enough coins to pay the fee: " + str(cost))
        else:
            shop_bought[3] += 1
            wallet -= cost
            print("Bought a level!")
            level += 1
            check_level(level)

# Main loop, to loop through the program and continue to gather inputs from the user.
while True:
    # Checks if the user is too in debt; if so, the game ends immediately.
    if wallet < -10000:
        print("You are too in debt, and the game is now over.")
        break
    # If the user is in debt, the user gets warned.
    if wallet < 0:
        print("You are now in debt. Be careful: if you are too much in debt, the game will end immediately!")
    # Check if the user has enough experience to level up.
    while exp >= 100:
        level += 1
        exp -= 100
        check_level(level)
    # Checks the user's achievements.
    achs_check()
    # Checks if the user is a millionare.
    if wallet > 1000000 and not mil_coins:
        print("You got the title Millionare!")
        title = "Millionare"
        mil_coins = True
    # Input the user for what they want to do.
    cmd = input("What do you want to do? ('quit' to quit and 'help' to view a list of commands) ").lower()
    # If the user quits, there is a final confirmation, and then the program exits.
    if cmd == "quit":
        confirm = input("Are you sure you want to quit? (type 'yes' to quit) ").lower()
        if "yes" in confirm:
            print("Thank you for playing my game!")
            break
    # For the user to get help
    elif "help" == cmd:
        print(get_help())
    # For the user's profile
    elif "wallet" == cmd or "balance" == cmd or "profile" == cmd:
        balance()
    # Rock Paper Scissors game
    elif cmd == "rps" or cmd == "rock paper scissors":
        rock_paper_scissors()
    # Displays the user's statistics
    elif cmd == "statistics" or cmd =="stats":
        statistics()
    # Highlow game
    elif cmd == "highlow":
        highlow()
    # Coinflip game
    elif cmd == "coinflip":
        coinflip()
    # Guessing Game
    elif cmd == "guess" or cmd == "guessing game":
        guessing_game()
    # Adventure
    elif cmd == "adventure":
        adventure()
    # First cheat code
    elif cmd == "money":
        cheat_code(1)
    # Second cheat code
    elif cmd == "level":
        cheat_code(2)
    # Third cheat code
    elif cmd == "experience":
        cheat_code(3)
    # Shop
    elif cmd == "shop":
        shop()
    # Otherwise, the input is invalid.
    else:
        print("Invalid command.")