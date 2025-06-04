import random
print("Library of babel-inspired thingy")

letters = "abcdefghijklmnopqrstuvwxyz,.!?'\""
words = "abcdefghijklmnopqrstuvwxyz"
punct = ",.,,,,!?"
place = -1
vowel = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"
dictionary = [
    "cat",
    "rat",
    "fat",
    "this",
    "is",
    "hello",
    "why",
    "that"
    ]

def gen(size, letters = letters, syll = False, word=False):
    ans = ""
    if word: 
        for i in range(size):
            ans += random.choice(dictionary)
            if i != size - 1:
                ans += " "
        return ans
    if syll:
        b = -1
        for i in range(size):
            if (b < 0):
                ans += random.choice(cons)
            else:
                ans += random.choice(vowel)
            b *= -1
        return ans
    
    for i in range(size):
        ans += random.choice(letters)
        
    return ans

while 1:
    try:
        hexagon = int(input("Enter your hexagon number: "))
        if hexagon <= 0:
            raise KeyboardInterrupt("no.")
        print("There are four bookcases on the sides of the hexagon.")
        side = int(input("Enter which of four bookcases to choose: "))
        if side <= 0 or side > 4:
            raise KeyboardInterrupt("do not.")
        print("There are five layers on the bookcase.")
        shelf = int(input("Enter which of five layers on the bookcase to choose:"))
        if shelf <= 0 or shelf > 5:
            raise KeyboardInterrupt("stop.")
        print("There are 10 books on the layer.")
        book = int(input("Choose one of ten books to choose."))
        if book <= 0 or book > 10:
            raise KeyboardInterrupt("nada.")
        
        place = (hexagon * side * shelf * book) % (side + shelf + book * hexagon)
        random.seed(place)
        break
    except:
        print("Invalid. \n\n\n")
        
print("Title:", gen(random.randint(5, 25)))

print("\n\n\n\n\n\n\nPlease enter: 9923 3 3 1\n\n\n\n\n\n\n\n\n")
mode = input("syllable, word, or random? (syll,word,other)")
ss = mode == "syll"
ww = mode == "word"

i = 1
while 1:
    print(f"Page {i}: ")
    flag = True
    print("    ",end = "")
    for j in range(random.randint(100, 300)):
        size = 1
        if ss or not (ss or ww):
            size = random.randint(5, 7)
        c = gen(size, syll = ss, word=ww)
        if (flag):
            if (random.randint(1, 10) == 1):
                print("\n", end="    ")
            print(c.title(), end="")
            flag = False
        else:
            print(c.lower(), end = "")
        if (random.randint(1, 5) == 1):
            d = gen(1, letters=punct)
            if (d in ['.', '!', '?']):
                flag = True
            print(d, end = " ")
        else:
            print("", end=" ")
    input()
    print("\n" * 5)
    i += 1