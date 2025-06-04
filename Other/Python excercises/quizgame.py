# Minglang Du 6-B1
# Project 6
# 2/6/2023

score = 0
def isvalid(answer, correct, second):
    print()
    if answer == correct:
        if second:
            print("Your answer was correct! You have earned 5 points.")
        else:
            print("Your answer was correct! You have earned 10 points.")
        return 1
    elif answer in ('A', 'B', 'C', 'D'):
        print("Your answer was incorrect. Try harder next time.")
        return 0
    else:
        print("Your answer was invalid. It has to be either A, B, C, or D.")
        return -1
    print()
    
def ask(question, correct, second = False):
    global score
    print()
    ans = isvalid(input(question), correct, second)
    if ans == 1:
        if second:
            score += 5
        else:
            score += 10
        return True
    elif ans == -1:
        return ask(question, correct)
    else:
        if second:
            return False
        else:
            print("You get a second chance. Correct answers yield less points.")
            return ask(question, correct, second = True)
    
def quiz():
    global score
    score = 0
    print("""
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
    """)
    ask("""
    1. What is the largest company in Toasterworld?
    ---------------------------------
    A. Breadtoast  B. Toasters, inc.|
    C. Bread, inc. D. Reddit        |
    ---------------------------------
    """, 'B')
    ask("""
    2. What is the most controversial social media site?
    ------------------------
    A. Twitter B. Facebook |
    C. Pinterest D. Reddit |
    ------------------------
    """, 'A')
    ask("""
    3. Name a game platform.
    -------------------------
    A. Unity       B. Robot |
    C. Doki Doki  D. Reddit |
    -------------------------
    """, 'A')
    ask("""
    4. What is the cringiest social media site?
    ------------------------
    A. Reddit B. Instagram |
    C. Google+   D. TikTok |
    ------------------------
    """, 'D')
    ask("""
    5. Name a creepypasta that nearly shut down
    due to copyright issues.
    --------------------------
    A. Backrooms B. Local 58 |
    C. SCP      D. JOHN CENA |
    --------------------------
    """, 'C')
    ask("""
    6. What is number lore?
    --------------------------------------
    A. A series by MatPat     B. your mom|
    C. A naming system for animals D. bad|
    --------------------------------------
    """, 'D')
    ask("""
    7. What is the best pet?
    --------------------
    A. Cats  B. Turtles|
    C. Dogs D. Toasters|
    --------------------
    """, 'A')
    if ask("""
    8. Who is B1's science teacher?
    -------------------------------------------------
    A. Mrs. Chen                   B. Mrs. Rayaprolu|
    C. Mrs. Parker D. A dark matter-shooting sausage|
    -------------------------------------------------
    """, 'A'):
        ask("""
    8a. Who used to be B1's science teacher?
    ----------------------------------
    A. Mrs. Chen B. Mrs. Rayaprolu   |
    C. a hedgehog D. a boy named Sue |
    ----------------------------------
    """, 'B')
        
    ask("""
    9. Is a function good for your program?
    ------------------------------------------------
    A. Yes                                   B. No |
    C. Everything should be a function D. Sometimes|
    ------------------------------------------------
    """, 'D')

    print()
    print("Thank you for participating in Minglang's Quiz Game!")
    print(f"Your score was {score} out of 100. ")

# output all correct

"""
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
"""