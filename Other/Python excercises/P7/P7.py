import re
import random
import time
import quizgame
import sys

# list of responses to user input
"""
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
"""

replies = {"hi hello hai":"hi"}

def get_user_msg(): # gets user's message
    raw = input("\n<User> ")
    wordparsed = re.findall(r"[\w']+|[.,!?;:]", raw)
    # turns the input into a list of words
    # without punctuation
    return wordparsed
    
def bot_say(say):
    print('[Bot is typing...]')
    time.sleep(len(say) / 10)
    # makes realistic delays between bot messages
    print('<Bot>', say, end = '')

def bot_reply(msg, last_reply):
    global replies # get list of replies
    new_dict = {} # make new dictionary because you can't
    # directly modify replies because of a bug
    for i in replies.keys(): #copy over new dictionary
        new_dict[i] = replies[i] 
    for i in replies.keys():
        if last_reply in i.split():
            # learn from the user's replies
            # by adding them into the response map
            new_dict[i.lower()] += "|" + " ".join(msg)
        elif last_reply != None: # not first reply and last reply not in response map
            for j in last_reply.split():
                if not j.lower() in i.split() and j.lower() != " ".join(msg).lower():
                    # stops bot saying the same thing the user said
                    new_dict[j.lower()] = " ".join(msg)
    replies = new_dict #copy over the new dictionary
    for i in replies.keys():
        for j in msg:
            # check if the user msg is in the response map
            if j.lower() in i.split():
                a = random.choice(replies[i].split('|'))
                bot_say(a) 
                return a # return last reply
    reply = random.choice(random.choice(list(replies.values())).split("|"))
    bot_say(reply)
    return reply # return random reply if not in response map
 
last_reply = None
print("""
This chatbot is a chatbot which
can adapt to the user. On its own,
the chatbot can understand some co-
nversations, but cannot understand
most variations of language or slang.
It also doesn't specialize in something
specific. I hope you enjoy talking with it.
Type 'q' and enter to quit the chatbot.
""") # print introduction
while True:
    msg = get_user_msg() # get user message
    if msg == ['q']: # check if user wants to quit
        bot_say("Please don't exit. I don't want to die. ")
        a = get_user_msg()
        if 'yes' in a or 'yeah' in a or 'sure' in a or 'yup' in a:
            print("\n[Chat ended]", file = sys.stderr)
            break
        else:
            bot_say("Good! What do you want to chat about?")
            continue
    if 'game' in msg or 'games' in msg or 'quiz' in msg: # check if user wants to play quiz game
        bot_say("Want to play a quiz game?")
        a = get_user_msg()
        if 'yes' in a or 'yeah' in a or 'sure' in a or 'yup' in a:
            quizgame.quiz()
            continue
    last_reply = bot_reply(msg, last_reply) # store last reply so bot can adapt to user 

# testing
# includes talking to bot
# the quiz game
# and exiting
"""
This chatbot is a chatbot which
can adapt to the user. On its own,
the chatbot can understand some co-
nversations, but cannot understand
most variations of language or slang.
It also doesn't specialize in something
specific. I hope you enjoy talking with it.
Type 'q' and enter to quit the chatbot.


<User> hello
[Bot is typing...]
<Bot> Hai
<User> can i play a game
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
"""