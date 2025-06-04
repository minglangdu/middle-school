import re, time
global font
global author
author = "Ayden Sean Liu"
font = 0
def crazy_lib():
    print("Welcome to crazy lib! By: ", author)
    font = input("Enter some numbers! :  ")
    if int(font) == 329:
        print("ERR0R")
        print("PLEASE RETRY!")
    else:
        noun = input("Enter a name: ")
        g = input("he or she?: ")
        noun2 = input("Enter another name: ")
        g2 = input("he or she?: ")
        noun3 = input("Enter a place: ")
        noun4 = input("Enter another thing: ")
        noun5 = input("Enter another thing: ")
        noun6 = input("Enter another name: ")
        noun7 = input("Enter who your talking to: ")
        verb = input("Enter a action: ")
        verb2 = input("Enter another action: ")
        other = input("Add something to help the first action: ")
        link = input("Enter a linking verb: ")
        adj = input("Enter a adjective: ")
        adj2 = input("Enter another adjective: ")
        pastverb = input("Enter a past tense verb: ")
        time.sleep(0.8)
        print(                                                          )
        time.sleep(0.8)
        print("Dear ", noun7, ",")
        time.sleep(0.8)
        print(noun, "and", noun2, 'on', 'a', pastverb, "at", noun3, link, noun4, ".")
        time.sleep(0.8)
        print("Then", noun, "and", noun2, verb, noun5, ".")
        time.sleep(0.8)
        print(noun, "was", adj, "so", g, verb2, noun2, "!")
        time.sleep(0.8)
        print("I'm tired of this place, it is so", adj2, "!")
        time.sleep(1.6)
        print("Sincerely, ", noun6, ".")
