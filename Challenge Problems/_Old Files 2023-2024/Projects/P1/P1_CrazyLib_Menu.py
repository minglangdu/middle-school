import Terencelib, MinglangLib, Anishlib, Aydenlib, Cerisselib, ChloeLib, Clairelib, Dhanyaalib, Dishalib, EliseLib, Madeleinelib, Olivialib, Thiyageshlib, VictorLib
import sys
"""By Minglang"""
libs = [MinglangLib, Terencelib, Anishlib, Aydenlib, Cerisselib, ChloeLib, Clairelib, Dhanyaalib, Dishalib, EliseLib, Madeleinelib, Olivialib, Thiyageshlib, VictorLib]

print("Welcome to the ", end = '')
print("INSANITY ", end='', file=sys.stderr)
print("Crazy Lib Menu!\nBy Minglang")
choice = ''
def menu():
    print("Choose a number or input 'q' to quit. ")
    for i in range(1, len(libs) + 1):
        lib = libs[i - 1]
        if hasattr(lib, "author") and hasattr(lib, "crazy_lib"):
            print(str(i) + ". " + lib.author + "'s crazy lib.")
        else:
            print(str(i) + ". CORRUPTED LIB", file=sys.stderr)
    choice = input()
    if choice == 'q':
        return
    try:
        l = libs[int(choice) - 1]
        print("Using", l.author, "'s crazy lib...")
        l.crazy_lib()
    except:
        input("The lib is either corrupted or you entered an invalid input.")
    menu()
    
menu()
print("Thank you for using the ", end = '')
print("INSANITY ", end='', file=sys.stderr)
print("Crazy Lib Menu!\nBy Minglang")