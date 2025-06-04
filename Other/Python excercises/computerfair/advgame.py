# Minglang Du 6-B1
# Computer Fair
# 4/24/2023

import random

quest = ["slay the dragon in the mountain!", "get a golden hoard of treasure.", "get a mystical sword buried under the hill!"]
first = ["Bob", "Dan", "Ben", "Ryan"]
intro = ["your long-lost dad", "a friend of a friend of a .. never mind", "a self-aware npc"]
challenge = ["You see a sentient bridge. ", "A large army approaches you. ", "A dragon breathes fire on you. ", "You see an undead army. ",
             "You see your dad carrying the milk.", "Someone tries to cancel you.", "You are accused of being a karma-farmer."]
c = ["Use a shield", "Use a plank", "Use a rock", "Use a rainbow", "Use a pick", "Use Twitter", "Use memes", "Use reddit"]
fail = {"Use a shield":"The shield whacks you in the head.",
        "Use a plank":"You plank, and die of exhaustion",
        "Use a rock":"The rock Johnson grabs you. Wrong rock.",
        "Use a rainbow":"You slide on the rainbow into a pot of molten gold.",
        "Use a pick":"You accidentally mine yourself.",
        "Use Twitter":"You get canceled.",
        "Use memes":"You make yourself look like a basement-dwelling troll, which you are.",
        "Use reddit":"Your post gets reposted onto r/downvotedtooblivion, TWICE."
        }
succ = {"Use a shield":"You block the attacks with the shield.",
        "Use a plank":"You plank, and intimidate everyone.",
        "Use a rock":"Everyone stares in disbelief, giving you time to run.",
        "Use a rainbow":"You slide on the rainbow into a pot of gold.",
        "Use a pick":"You dig under them.",
        "Use Twitter":"You roast Elon Musk, allowing you to go past.",
        "Use memes":"Your meme makes everyone respect you.",
        "Use reddit":"Your post gets reposted on 69 subreddits."}

def adv():
    print("""
--------------------------
|Welcome to my adventure |
|game. You have to choose|
|the right choice to cont|
|-inue. The adventure is |
|randomized every time.  |
--------------------------
    """)
    name = random.choice(first)
    q = random.choice(quest)
    print("You meet up with " + name + ", " + random.choice(intro) + ".")
    print(name.title() + " tells you to " + q + ".")
    choice = input("A. 'Of course not!' B. 'Sure.'\n").lower()
    if choice == 'b':
        print("The man smiles.")
        print("You continue on with the quest!")
    elif choice == 'a':
        print("The man beats you up.\nYou are dead.")
        return
    else:
        print("Use A or B as an answer.")
        return
    for i in range(random.randint(5, 7)):
        print(random.choice(challenge))
        choices = []
        while len(choices) < 3:
            temp = random.choice(c)
            if temp in choices:
                continue
            else:
                choices.append(temp)
        choice = input("A. " + choices[0] + " B. " + choices[1] + " C. " + choices[2] + "\n").lower()
        if choice == "a":
            choice = choices[0]
        elif choice == "b":
            choice = choices[1]
        elif choice == "c":
            choice = choices[2]
        else:
            print("Use A or B as an answer.")
            return
        if random.randint(1,10) < 5:
            print(fail[choice])
            print("You are dead.")
            return
        else:
            print(succ[choice])
            print("You continue on with the quest!")
    print("You complete the quest!")
    print("You win!")
    return
if __name__ == "__main__":
    adv()