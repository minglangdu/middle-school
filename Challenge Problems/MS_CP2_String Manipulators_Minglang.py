def printc(string, string2):
    print("Original string:", string)
    print("New string:", string2)
    print()

print("_Problem 1: Reverse_")
def reverse(string):
    str2 = ""
    for i in range(len(string) - 1, -1, -1):
        str2 += string[i]
    return str2
string = "Little by little, one travels far. --J.R.R. Tolkien"
printc(string, reverse(string))
string = "Look at a stone cutter hammering away at his rock, perhaps a hundred times without as much as a crack showing in it. Yet at the hundred-and-first blow it will split in two, and I know it was not the last blow that did it, but all that had gone before. -- Jacob Riis"
printc(string, reverse(string))

print("_Problem 2: Title Case Converter_")
def titlec(string):
    str2 = ""
    list = string.split()
    for i in list:
        str2 += i.title() + " "
    return str2[:-1]
string = "jaws 10: only two teeth left"
printc(string, titlec(string))

print("_Problem 3: Letter Frequency Counter_")
def pangram(string):
    for i in range(97, 123):
        if (string.find(chr(i)) < 0):
            return False
    return True
def freq(string):
    mp = {}
    for i in range(97, 123):
        mp[chr(i)] = [0, 0]
    for c in string:
        if (c in mp):
            mp[c][0] += 1
    for i in range(97, 123):
        mp[chr(i)][1] = round(mp[chr(i)][0] / len(string),3)
    return mp
        

def printa(string):
    print("-" * 38)
    print("String to be Analyzed:", string)
    print("-" * 38)
    print("Letter Frequency Table:")
    print("-" * 38)
    print("Letter     Count     Percentage")
    print("-" * 38)
    string = string.lower()
    mp = freq(string)
    for i in range(97, 123):
        print(chr(i).ljust(10) +
              str(mp[chr(i)][0]).ljust(10) +
              (str(round(mp[chr(i)][1] * 100, 1)) + "%").ljust(10))
    print()
    if (pangram(string)):
        print("The string has all the letters in the alphabet! If it is a sentence, it is a pangram.")
    else:
        print("The string does not have all the letters in the alphabet. It is not a pangram.")
        
string = "SPHINX OF BLACK QUARTZ, JUDGE MY VOW! Waxy and quivering, jocks fumble the pizza. Is it the job of the wizard to vex the chumps quickly in fog?"
printa(string)
string = """"I have, myself, full confidence that if all do their duty, if nothing is neglected, and if the best arrangements are made, as they are being made, we shall prove ourselves once again able to defend our Island home, to ride out the storm of war, and to outlive the menace of tyranny, if necessary for years, if necessary alone. At any rate, that is what we are going to try to do. That is the resolve of His Majesty’s Government-every man of them. That is the will of Parliament and the nation. The British Empire and the French Republic, linked together in their cause and in their need, will defend to the death their native soil, aiding each other like good comrades to the utmost of their strength. Even though large tracts of Europe and many old and famous States have fallen or may fall into the grip of the Gestapo and all the odious apparatus of Nazi rule, we shall not flag or fail. We shall go on to the end, we shall fight in France, we shall fight on the seas and oceans, we shall fight with growing confidence and growing strength in the air, we shall defend our Island, whatever the cost may be, we shall fight on the beaches, we shall fight on the landing gstr(rounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender, and even if, which I do not for a moment believe, this Island or a large part of it were subjugated and starving, then our Empire beyond the seas, armed and guarded by the British Fleet, would carry on the struggle, until, in God’s good time, the New World, with all its power and might, steps forth to the rescue and the liberation of the old." --Winston Churchill"""
printa(string)

print("_Problem 4. Pig Latin Translator_")
def pigl(string):
    str2 = ""
    list = string.split()
    for i in list:
        punct = i[-1]
        if (not punct.isalpha()):
            i = i[:-1]
        else:
            punct = ""
        first = i[0].lower()
        if (first not in ['a', 'e', 'i', 'o', 'u']):
            i = i[1:]
            i += first
        i += "ay"
        i += punct
        str2 += i + " "
    return str2[:-1]

string = "Little by little, one travels far. --J.R.R. Tolkien "
printc(string, pigl(string))
string = "Look at a stone cutter hammering away at his rock, perhaps a hundred times without as much as a crack showing in it. Yet at the hundred-and-first blow it will split in two, and I know it was not the last blow that did it, but all that had gone before. -- Jacob Riis "
printc(string, pigl(string))