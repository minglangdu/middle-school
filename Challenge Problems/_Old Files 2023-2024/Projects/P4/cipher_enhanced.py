import random

alts = "☺☻♥♦♣♠•◘○◙♂♀♪♫"
def encrypt_char(c): # encrypt a single character
    a = '' # default
    if c == "A":
        a = "W"
    if c == "B":
        a = "h"
    if c == "C":
        a = "e"
    if c == "D":
        a = "N"
    if c == "E":
        a = "t"
    if c == "F":
        a = "H"
    if c == "G":
        a = "a"
    if c == "H":
        a = "T"
    if c == "I":
        a = "G"
    if c == "J":
        a = "3"
    if c == "K":
        a = "o"
    if c == "L":
        a = "A"
    if c == "M":
        a = "u"
    if c == "N":
        a = "z"
    if c == "O":
        a = "Q"
    if c == "P":
        a = "K"
    if c == "Q":
        a = "x"
    if c == "R":
        a = "D"
    if c == "S":
        a = "X"
    if c == "T":
        a = "s"
    if c == "U":
        a = "S"
    if c == "V":
        a = "U"
    if c == "W":
        a = "n"
    if c == "X":
        a = "v"
    if c == "Y":
        a = "Z"
    if c == "Z":
        a = "C"
    if c == "a":
        a = random.choice(["7", alts[0]]) 
    if c == "b":
        a = "1"
    if c == "c":
        a = "9"
    if c == "d":
        a = random.choice(["5", alts[1]]) 
    if c == "e":
        a = random.choice(["c", alts[2]]) 
    if c == "f":
        a = "k"
    if c == "g":
        a = "g"
    if c == "h":
        a = random.choice(["I", alts[3]]) 
    if c == "i":
        a = random.choice(["F", alts[4]]) 
    if c == "j":
        a = " "
    if c == "k":
        a = ","
    if c == "l":
        a = random.choice(["/", alts[5]]) 
    if c == "m":
        a = "O"
    if c == "n":
        a = random.choice(["q", alts[6]]) 
    if c == "o":
        a = random.choice(["L", alts[7]]) 
    if c == "p":
        a = "d"
    if c == "q":
        a = "B"
    if c == "r":
        a = random.choice(["J", alts[8]]) 
    if c == "s":
        a = random.choice(["!", alts[9]]) 
    if c == "t":
        a = random.choice([".", alts[10]]) 
    if c == "u":
        a = "-"
    if c == "v":
        a = "0"
    if c == "w":
        a = "y"
    if c == "x":
        a = "w"
    if c == "y":
        a = "b"
    if c == "z":
        a = "E"
    if c == "0":
        a = ":"
    if c == "1":
        a = "l"
    if c == "2":
        a = ";"
    if c == "3":
        a = "m"
    if c == "4":
        a = "8"
    if c == "5":
        a = "6"
    if c == "6":
        a = "2"
    if c == "7":
        a = "Y"
    if c == "8":
        a = "P"
    if c == "9":
        a = "M"
    if c == " ":
        a = random.choice(["R", alts[13]]) 
    if c == ",":
        a = random.choice(["p", alts[11]]) 
    if c == ".":
        a = random.choice(["V", alts[12]]) 
    if c == "!":
        a = "r"
    if c == "?":
        a = "4"
    if c == "/":
        a = "?"
    if c == "-":
        a = "f"
    if a: # in array
        return a
    else:
        return c
    
def decrypt_char(c): # similar to encrypt_char, but does the opposite
    a = ''
    if c == "W":
        a = "A"
    if c == "h":
        a = "B"
    if c == "e":
        a = "C"
    if c == "N":
        a = "D"
    if c == "t":
        a = "E"
    if c == "H":
        a = "F"
    if c == "a":
        a = "G"
    if c == "T":
        a = "H"
    if c == "G":
        a = "I"
    if c == "3":
        a = "J"
    if c == "o":
        a = "K"
    if c == "A":
        a = "L"
    if c == "u":
        a = "M"
    if c == "z":
        a = "N"
    if c == "Q":
        a = "O"
    if c == "l":
        a = "1"
    if c == ";":
        a = "2"
    if c == "m":
        a = "3"
    if c == "8":
        a = "4"
    if c == "6":
        a = "5"
    if c == "2":
        a = "6"
    if c == "Y":
        a = "7"
    if c == "P":
        a = "8"
    if c == "M":
        a = "9"
    if c == "R":
        a = " "
    if c == "p":
        a = ","
    if c == "V":
        a = "."
    if c == "r":
        a = "!"
    if c == "4":
        a = "?"
    if c == "?":
        a = "/"
    if c == "f":
        a = "-"
        a = "O"
    if c == "K":
        a = "P"
    if c == "x":
        a = "Q"
    if c == "D":
        a = "R"
    if c == "X":
        a = "S"
    if c == "s":
        a = "T"
    if c == "S":
        a = "U"
    if c == "U":
        a = "V"
    if c == "n":
        a = "W"
    if c == "v":
        a = "X"
    if c == "Z":
        a = "Y"
    if c == "C":
        a = "Z"
    if c == "7" or c == alts[0]:
        a = "a"
    if c == "1":
        a = "b"
    if c == "9":
        a = "c"
    if c == "5" or c == alts[1]:
        a = "d"
    if c == "c" or c == alts[2]:
        a = "e"
    if c == "k":
        a = "f"
    if c == "g":
        a = "g"
    if c == "I" or c == alts[3]:
        a = "h"
    if c == "F" or c == alts[4]:
        a = "i"
    if c == " ":
        a = "j"
    if c == ",":
        a = "k"
    if c == "/" or c == alts[5]:
        a = "l"
    if c == "O":
        a = "m"
    if c == "q" or c == alts[6]:
        a = "n"
    if c == "L" or c == alts[7]:
        a = "o"
    if c == "d":
        a = "p"
    if c == "B":
        a = "q"
    if c == "J" or c == alts[8]:
        a = "r"
    if c == "!" or c == alts[9]:
        a = "s"
    if c == "." or c == alts[10]:
        a = "t"
    if c == "-":
        a = "u"
    if c == "0":
        a = "v"
    if c == "y":
        a = "w"
    if c == "w":
        a = "x"
    if c == "b":
        a = "y"
    if c == "E":
        a = "z"
    if c == ":":
        a = "0"
    if c == "l":
        a = "1"
    if c == ";":
        a = "2"
    if c == "m":
        a = "3"
    if c == "8":
        a = "4"
    if c == "6":
        a = "5"
    if c == "2":
        a = "6"
    if c == "Y":
        a = "7"
    if c == "P":
        a = "8"
    if c == "M":
        a = "9"
    if c == "R" or c == alts[13]:
        a = " "
    if c == "p" or c == alts[11]:
        a = ","
    if c == "V" or c == alts[12]:
        a = "."
    if c == "r":
        a = "!"
    if c == "4":
        a = "?"
    if c == "?":
        a = "/"
    if c == "f":
        a = "-"
    if a:
        return a
    else:
        return c
    
def encrypt(s): # loops through characters, encrypting each 
    new = ""
    for c in s:
        new += encrypt_char(c)
    return new

def decrypt(s): # loops through characters, decrypting each
    new = ""
    for c in s:
        new += decrypt_char(c)
    return new