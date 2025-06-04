# Minglang Du 6-B1
# Computer Fair
# 4/24/2023

import re
import random
import time
import quizgame
import advgame
import sys

# reply map
replies = {"hi hello":"What's up?|Hai",
           "food apple orange drink juice fries":"I like eating|I want to go to lunch",
           "no nope n":"Okay|Fine",
           "y yes yeah yup ok sure okay":"good|thanks",
           "huh hmm":"You don't understand?|I don't understand too",
           "therapy depressed emo":"I don't need therapy|Huh?|Are you good?",
           "hurt ouch pain":"Are you good?|I'm sorry",
           "sorry":"That's okay",
           "earth planet sun moon universe":"I don't know what that is|What is the solar system?",
           "family parents mom dad sibling brother sister":"I can't have a family|I'm a bot|period period period haha",
           "person people human humans":"Are you a human?|You're a person",
           "life live lives":"I have no life",
           "bot program matrix":"No I'm not|You are|Your mom is a bot",
           "twitter tiktok youtube internet":"I don't understand the internet|What is the internet",
           "thanks thank":"You are welcome|Yay!"
           }

def get_user_msg():
    raw = input("\n<User> ")
    wordparsed = re.findall(r"[\w']+|[.,!?;:]", raw)
    return wordparsed
    
def bot_say(say):
    print('[Bot is typing...]')
    time.sleep(len(say) / 10)
    print('<Bot>', say, end = '')

def bot_reply(msg, last_reply):
    global replies
    new_dict = {}
    for i in replies.keys():
        new_dict[i] = replies[i]
    for i in replies.keys():
        if last_reply in i.split():
            new_dict[i.lower()] += "|" + " ".join(msg)
        elif last_reply != None:
            for j in last_reply.split():
                if not j.lower() in i.split() and j.lower() != " ".join(msg).lower():
                    new_dict[j.lower()] = " ".join(msg)
    replies = new_dict
    for i in replies.keys():
        for j in msg:
            if j.lower() in i.split():
                a = random.choice(replies[i].split('|'))
                bot_say(a)
                return a
    reply = random.choice(random.choice(list(replies.values())).split("|"))
    bot_say(reply)
    return reply
 
def loop():
    last_reply = None
    while True:
        msg = get_user_msg()
        if msg == ['q']:
            bot_say("Really quit?")
            a = get_user_msg()
            if 'yes' in a or 'yeah' in a or 'sure' in a or 'yup' in a:
                bot_say("Thank you for talking with me!")
                print("\n[Chat ended]", file = sys.stderr)
                print("Do you want to save this chatbot's memory? (y = yes)")
                b = get_user_msg()
                if 'y' in b:
                    print("Copy: ")
                    for i in replies:
                        print(i)
                        print(replies[i])
                break
            else:
                bot_say("Good! What do you want to chat about?")
                continue
        if 'game' in msg or 'games' in msg or 'quiz' in msg:
            bot_say("Want to play a quiz game?")
            a = get_user_msg()
            if 'yes' in a or 'yeah' in a or 'sure' in a or 'yup' in a:
                quizgame.quiz()
                continue
            else:
                bot_say("An adventure game?")
                a = get_user_msg()
                if 'yes' in a or 'yeah' in a or 'sure' in a or 'yup' in a:
                    advgame.adv()
                    continue
        last_reply = bot_reply(msg, last_reply)
print("""
+--------------------------------------------+
| This chatbot is a chatbot which            |
| can adapt to the user. On its own,         |
| the chatbot can understand some co-        |
| nversations, but cannot understand         |
| most variations of language or slang.      |
| It also doesn't specialize in something    |
| specific. I hope you enjoy talking with it.|
| Type 'q' and enter to quit the chatbot.    |
+--------------------------------------------+
""")
if input("Do you want to load a chatbot? (y=yes) (press q twice when you are done)") == "y":
    replies = {}
    a = ''
    while a != 'q':
        a = input()
        b = input()
        replies[a] = b
    del replies['q']

loop()


# output
"""
+--------------------------------------------+
| This chatbot is a chatbot which            |
| can adapt to the user. On its own,         |
| the chatbot can understand some co-        |
| nversations, but cannot understand         |
| most variations of language or slang.      |
| It also doesn't specialize in something    |
| specific. I hope you enjoy talking with it.|
| Type 'q' and enter to quit the chatbot.    |
+--------------------------------------------+

Do you want to load a chatbot? (y=yes) (press q twice when you are done)y
hi
asdf
b
tasdf
q
q

<User> hi
[Bot is typing...]
<Bot> asdf
<User> b
[Bot is typing...]
<Bot> tasdf
<User> can i play a game?
[Bot is typing...]
<Bot> Want to play a quiz game?
<User> no
[Bot is typing...]
<Bot> An adventure game?
<User> yes

--------------------------
|Welcome to my adventure |
|game. You have to choose|
|the right choice to cont|
|-inue. The adventure is |
|randomized every time.  |
--------------------------
    
You meet up with Ben, your long-lost dad.
Ben tells you to slay the dragon in the mountain!.
A. 'Of course not!' B. 'Sure.'
A
The man beats you up.
 You are dead.

<User> let's play another game
[Bot is typing...]
<Bot> Want to play a quiz game?
<User> yes

Welcome to Minglang's Quiz Game!
----------------------------------
| You will be given 10 multiple  |
| choice questions. A correct    |
| answer yields 10 points. Re-   |
| trys will yield less points.   |
| There are some bonus questions |
| that also give points. The num |
| ber of bonus questions is secr |
| et. Good Luck!                 |
----------------------------------





1. What is the largest company in Toasterworld?
---------------------------------
A. Breadtoast  B. Toasters, inc.|
C. Bread, inc. D. Reddit        |
---------------------------------
B

Your answer was correct! You have earned 10 points.


2. What is the most controversial social media site?
------------------------
A. Twitter B. Facebook |
C. Pinterest D. Reddit |
------------------------
A

Your answer was correct! You have earned 10 points.


3. Name a game platform.
-------------------------
A. Unity       B. Robot |
C. Doki Doki  D. Reddit |
-------------------------
A

Your answer was correct! You have earned 10 points.


4. What is the cringiest social media site?
------------------------
A. Reddit B. Instagram |
C. Google+   D. TikTok |
------------------------
D

Your answer was correct! You have earned 10 points.


5. Name a creepypasta that nearly shut down
due to copyright issues.
--------------------------
A. Backrooms B. Local 58 |
C. SCP      D. JOHN CENA |
--------------------------
C

Your answer was correct! You have earned 10 points.


6. What is number lore?
--------------------------------------
A. A series by MatPat     B. your mom|
C. A naming system for animals D. bad|
--------------------------------------
D

Your answer was correct! You have earned 10 points.


7. What is the best pet?
--------------------
A. Cats  B. Turtles|
C. Dogs D. Toasters|
--------------------
A

Your answer was correct! You have earned 10 points.


8. Who is B1's science teacher?
-------------------------------------------------
A. Mrs. Chen                   B. Mrs. Rayaprolu|
C. Mrs. Parker D. A dark matter-shooting sausage|
-------------------------------------------------
A

Your answer was correct! You have earned 10 points.


8a. Who used to be B1's science teacher?
----------------------------------
A. Mrs. Chen B. Mrs. Rayaprolu   |
C. a hedgehog D. a boy named Sue |
----------------------------------
B

Your answer was correct! You have earned 10 points.


9. Is a function good for your program?
------------------------------------------------
A. Yes                                   B. No |
C. Everything should be a function D. Sometimes|
------------------------------------------------
D

Your answer was correct! You have earned 10 points.

Thank you for participating in Minglang's Quiz Game!
Your score was 100 out of 100. 

<User> q
[Bot is typing...]
<Bot> Really quit?
<User> yes
[Bot is typing...]
<Bot> Thank you for talking with me!
[Chat ended]
Do you want to save this chatbot's memory? (y = yes)

<User> y
Copy: 
hi
asdf
b
tasdf
asdf
b
"""