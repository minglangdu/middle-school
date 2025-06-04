"""
Project 3: Physics Problems
Student: Minglang Du
Class: 7-C6
"""

# Problem 1

def half_life():
    # introduce calculator
    print("Welcome to the half-life calculator.\n" + '-' * 30 + "\nEnter values without units. \nUnits are entered separately.")
    # ask for input
    name = input("Enter the name of your substance: ") # substance name
    hl_u = input("Enter the unit in which half-life is measured: ") # half-life unit
    hl = input("Enter the approximate half-life in " + hl_u + " (rounded down): ") # half-life
    m_u = input("Enter the unit in which mass is measured: ") # mass unit
    m = input("Enter the approximate mass in " + m_u + " (rounded down): ") # mass
    e = input("Enter the target ending mass in " + m_u + ": ") # target
    print("\nHalf-Life Table for " + name.title() + ": " + m + " " + m_u + " to " + e + " " + m_u) # title of table
    print("_" * 72)
    print("Half-Lives Elapsed".ljust(24) + ("Time Elapsed (" + hl_u + ")").ljust(24) + \
          (name.title() + " Amount (" + m_u + ")").ljust(24))
    print("_" * 72)
    
    am = float(m) # mass of remaining substance
    hl_elapsed = 0 # half-lives passed
    elapsed = 0 # time passed
    while am > float(e): # while amount is greater than target
        print(str(hl_elapsed).ljust(24) + str(elapsed).ljust(24) + str(am).ljust(24))
        hl_elapsed += 1
        elapsed += float(hl)
        am /= 2 # half decayed
    print(str(hl_elapsed).ljust(24) + str(elapsed).ljust(24) + str(am).ljust(24))
    
# Problem 2

def time_dilation():
    from math import sqrt
    # introduce calculator
    print("Time Dilation Calculator\n" + "-" * 72 + "\nEnter all values without units" \
          +"\nYou will be prompted for units separately. ")
    # ask for values
    length = float(input("Enter the length of interstellar travel time: ")) # observer time
    l_u = input("Enter the unit of time: ") # observer time unit
    print("\nTime Dilation Table\n" + "-"*100) # table title
    print("Percent of Light Speed".ljust(25) + "Travel Time".ljust(25) + \
          "Time Dilation".ljust(25) + "Earth Time".ljust(25) + "\n" + "-" * 100)
    
    ls = 10 # light fraction
    dil = 1.0 # time dilation
    et = length # earth time (observer)
    while ls < 100:
        et = round(length / sqrt(1 - (ls/100)**2), 2) # use equation
        dil = round(length / et, 2) # pObserver / pTraveler
        print(str(ls).ljust(25) + (str(length) + " " + l_u).ljust(25) + ("x " + str(dil)).ljust(25) + \
              (str(et) + " " + l_u).ljust(25))
        if ls < 90:
            ls += 10 # increment by ten
        else:
            ls += 1 # then increment by 1 when 90 is reached
    
# Problem 3 (Challenge)

c = None # choice
print("Physics Calculator Menu\n" + "-" * 72 + "\nChoose from one of the following option" \
          +"\n  1. Calculate from a half-life/substance decay table.\n  2. Calculate a time dilation table." +\
      "\n  3. Quit.\n\n")
while c != '3': 
    c = input("Enter the number of your choice: ")
    if c == '1':
        half_life() # run half life
    elif c == '2':
        time_dilation() # run time dilation
    elif c != '3': # neither 1, 2, nor 3
        print("Invalid input. Please try again.")