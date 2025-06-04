import sys

author = "Minglang Du"

def crazy_lib():
    titles = {"Terrible Vacation":1, "'This Is Not A Drill!'":2, "Worst Day Ever":3}
    libs = ["""Today, me and _name_ had a vacation. We took the _mode of transport_ to _location_.
    It was the most _adjective_ vacation ever! First, the hotels were _adjective_. Also, there were
    no _adjective_ places to go. I wanted to go to _location_ but it was 'too _adjective_'. The other person
    _past tense verb_ all the time there. I never want to _verb_ again because of that place. 
    Please _verb_ me.""",
            """I almost _past tense verb_ today! I was in class,
    _present perfect verb_ when the fire _noun_ rang! I thought it was a _noun_,
    so I continued _present perfect verb_. Then, _dangerous thing_ came in! I
    realized this was an _event_! Everyone was already _adjective_, except me and
    _name_. Then, _name_ crashed in and saved us with _noun_. I am still _adjective_.""",
            """Today was a very _adjective_ day! I woke up and I was already _adjective_!
    Then, _name_ came _present participle_ in my room! I was already _adjective_, but then
    I realized I had to go to _location_. There, I saw my worst _noun_, _name_. I hated
    that _noun_! I hate this day so much and I never want to _verb_ again. THE END"""]

    choices = []
    choice = ''
    # Story selection code
    print("Welcome to ", end = '')
    print("INSANITY LIBS", end = '', file = sys.stderr)
    print("!\nBy Minglang")
    print("Please select a story.")
    for i in titles.keys():
        print(str(titles[i]) + ". " + i)
    try:
        choice = int(input())
    except:
        pass
    while not choice in titles.values():
        print("Invalid choice. ")
        try:
            choice = int(input())
        except:
            pass
    lib = libs[choice - 1]
    # Choosing words code
    print("Starting crazy lib...")
    print("\nPlease enter a random word with the part of speech given.")
    reading = False
    part = ''
    for i in range(0, len(lib)):
        if reading == False and lib[i] == '_':
            reading = True
        elif reading == True and lib[i] != '_':
            part += lib[i]
        elif reading == True:
            reading = False
            choices.append(input("Enter a " + part + ": "))
            part = ''
    # Outputting story code
    print("Story:\n")
    word = 0
    for i in range(0, len(lib)):
        if reading == False and lib[i] != '_':
            print(lib[i], end = '')
        elif reading == False and lib[i] == '_':
            print(choices[word], end = '', file = sys.stderr)
            word += 1
            reading = True
        elif reading == True and lib[i] == '_':
            reading = False
    # Replaying code        
    print("\nThank you for playing Insanity Libs!")
    replay = input("Enter 'a' to replay! ")
    if replay == 'a':
        choices = []
        crazy_lib()