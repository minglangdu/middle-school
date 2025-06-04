"""
Terence Wang 7-C6
Project 1: Crazy Libs
"""
author = "Terence Wang"
def crazylibs():
    """
    The main function file to run the program (and import into other programs).
    """
    # Introduction
    print("Welcome to " + author + "'s CrAzY lIbS!")
    # All of the user inputs for the crazy libs. They are stored in various variables.
    student = input("Enter a student name: ")
    adjective1 = input("Enter an adjective: ")
    time = input("Enter a unit of time: ")
    subject = input("Enter a subject in school: ")
    adjective2 = input("Enter an adjective: ")
    score = input("Enter a number: ")
    verb1 = input("Enter a transitive verb: ")
    place = input("Enter the name of a location: ")
    assignment = input("Enter a name of a school assignment: ")
    verb2 = input("Enter a transitive verb: ")
    noun = input("Enter a noun: ")
    verb3 = input("Enter another transitive verb: ")
    noun2 = input("Enter another noun: ")
    number = input("Enter a number: ")
    verbing = input("Enter a gerund: ")
    greeting = input("Enter a greeting: ")
    name = input("Enter another student name: ")
    # Prints out the final result.
    print("----------------------------------------------------------------")
    print("Dear " + student + ",")
    print("I am here to tell you how " + adjective1 + " you have been so far this " + time + ".")
    print("Your grades in " + subject + " have been so " + adjective2 + " that your average score was " + score + "!")
    print("Because of this, I would like to " + verb1 + " you from my " + place + ".")
    print("Just look at this " + assignment + ": you forgot how to " + verb2 + " this " + noun + ".")
    print("Also, you haven't " + verb3 + " your " + noun2 + " yet, so you basically got " + number + " months of " + verbing + " for free!")
    print(greeting + ",")
    print(name)

# crazylibs()