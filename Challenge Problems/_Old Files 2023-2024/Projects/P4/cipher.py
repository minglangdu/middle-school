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
        a = "7"
    if c == "b":
        a = "1"
    if c == "c":
        a = "9"
    if c == "d":
        a = "5"
    if c == "e":
        a = "c"
    if c == "f":
        a = "k"
    if c == "g":
        a = "g"
    if c == "h":
        a = "I"
    if c == "i":
        a = "F"
    if c == "j":
        a = " "
    if c == "k":
        a = ","
    if c == "l":
        a = "/"
    if c == "m":
        a = "O"
    if c == "n":
        a = "q"
    if c == "o":
        a = "L"
    if c == "p":
        a = "d"
    if c == "q":
        a = "B"
    if c == "r":
        a = "J"
    if c == "s":
        a = "!"
    if c == "t":
        a = "."
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
        a = "R"
    if c == ",":
        a = "p"
    if c == ".":
        a = "V"
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
    if c == "7":
        a = "a"
    if c == "1":
        a = "b"
    if c == "9":
        a = "c"
    if c == "5":
        a = "d"
    if c == "c":
        a = "e"
    if c == "k":
        a = "f"
    if c == "g":
        a = "g"
    if c == "I":
        a = "h"
    if c == "F":
        a = "i"
    if c == " ":
        a = "j"
    if c == ",":
        a = "k"
    if c == "/":
        a = "l"
    if c == "O":
        a = "m"
    if c == "q":
        a = "n"
    if c == "L":
        a = "o"
    if c == "d":
        a = "p"
    if c == "B":
        a = "q"
    if c == "J":
        a = "r"
    if c == "!":
        a = "s"
    if c == ".":
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

