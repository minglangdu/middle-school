"""
Quiz #4: Chapter 10
Problem Code and Solutions
Python Level 2

***
Students: copy this file from LabCommons into your H:\ drive and
replace "Student Code" in the file name with your user name
(e.g., MS2_Quiz4_JohnD.py). Rename a file by selecting it and
pressing F2. The file must be closed to do this.

FILL IN THE FIELDS BELOW AND SUBMIT A PRINTOUT
OF THIS FILE WITH YOUR QUIZ PAPER

Following these instructions is worth 1 point.
***

Name: Minglang Du
Grade/Section: G7-C6
Date: February 5, 2024

"""

print('\n*** Problem 1 ***')           # 15 points

# Add code to the line with a # to finish defining space_out(). This 
# should print each character in string s with an extra space added
# between each of its characters.
# Remove the """ before and after the code to run it.

def space_out(s):
    for ch in s:
        print(ch, end=' ')


# Add two test cases to ensure the function works as intended:
print("String 1: hello world\nSpaced out: ", end='')
space_out("hello world")
print()
print("String 2: this is spaced out\nSpaced out: ", end='')
space_out("this is spaced out")
print()

print('\n\n*** Problem 2 ***')         # 15 points

# Redefine space_out() below to return the spaced-out string in a
# variable new_string (instead of just printing it).
# You will need to add code on every line with a #.
def space_out(s):
    new_string = ""
    for ch in s:
        new_string += ch + ' '
    return new_string
    

# Copy-paste the same two test cases from #1 below to ensure the
# function still works as intended:
print("String 1: hello world\nSpaced out: ", end='')
print(space_out("hello world"))

print("String 2: this is spaced out\nSpaced out: ", end='')
print(space_out("this is spaced out"))


print('\n*** Problem 3 ***')           # 15 points

# Define trim() to return a slice of the string contained in its
# parameter whole. That slice must exclude the first and last 
# characters but keep everything else. (Thus, if whole has 2 or
# fewer characters, trim() should not output anything.)

def trim(whole):
    new_string = ""
    for i in range(1, len(whole) - 1):
        new_string += whole[i]
    return new_string

# Add three test cases below with strings of 1, 2, and 4+ characters.
print("String 1: a\nTrimmed: ", trim('a'))
print("String 2: ab\nTrimmed: ", trim('ab'))
print("String 3: hello there\nTrimmed: ", trim('hello there'))


print('\n*** Problem 4 ***')           # 20 points

"""
Some programming languages, such as Java, follow a naming convention
called "camel case," in which words in identifiers are separated by
capitalizing their first letters. The first letter of the first word
may or may not be capitalized, depending on what the name represents.
For example: portOfOrigin or LocationMap. 

Python does not follow camel case; instead it follows 'underscore
case', in which words are separated by an underscore. This is
generally easier to read. For this problem, write a function called
und_case() that accepts a string parameter s containing a group of
words in camel case. The function should convert those words into
underscore case and return the resulting string. Leave the first
letter's case unchanged and don't add an underscore before it. Test
your function with strings of multiple camel case words with both an
upper- and lowercase first letter. 
"""

def und_case(s):
    new_string = s[0]
    for i in range(1, len(s)):
        if s[i].isupper():
            new_string += '_'
        new_string += s[i].lower()
    return new_string

# Add two camel case test cases below, one string starting with a
# capital letter and another starting with a lowercase letter.
print("String 1: portOfOrigin\nUnderscore case: ", und_case('portOfOrigin'))
print("String 2: LocationOfObject\nUnderscore case: ", und_case('LocationOfObject'))


print('\n*** Problem 5 ***')           # 16 points (4 per bug)

# Debug the code in char_ratios() until it works as intended.
# Find and fix all four bugs.

# char_ratios should print out the percentage of a string's characters
# that are vowels, the percentage that are consonants, and the per-
# centage that are neither, rounded to the nearest tenth of a percent.

def char_ratios(s):
    s_length = len(s)
    vowel_count = 0
    cons_count = 0
    other_count = 0
    for ch in s.lower(): # a colon was missing in this for loop
        if ch in 'aeiou':
            vowel_count += 1 # these three statements used to not add to the count
        elif ch in 'bcdfghjklmnpqrstvwxyz':
            cons_count += 1
        else:
            other_count += 1 # other_count was not defined before the loop
    v_percent = round(vowel_count / s_length, 1)
    c_percent = round(cons_count / s_length, 1)
    o_percent = round(other_count / s_length, 1)
    print('The string "' + s + '" is roughly', v_percent * 100, '% vowels,',
          c_percent * 100, '% consonants, and', # the decimals weren't converted 
          o_percent * 100, '% non-letter characters.') # to percents

# Test cases are provided:
char_ratios('The Warriors are inevitable.')
char_ratios('Beware! The roads are icy this time of year.')
char_ratios('The quick brown fox jumps over the lazy dog.')



print('\n*** Problem 6 ***')           # 18 points (9 per comment)

# Study and test the following functions to figure out how they work.
# Add a comment above each function to explain what each does and how
# it works.

# This function checks if the string is all numbers, and whether you can
# convert it to an integer case
def can_int_str(s):
    for ch in s:
        if ch in '0123456789':
            continue
        else:
            return False
    return True

# This function checks if the string can be turned into an integer, then
# does so if it is possible to.
def make_int(s):
    if can_int_str(s):
        return int(s)
    else:
        return False       

# Test cases are provided:
print('can_int_str(\'12334325f\'):', can_int_str('12334325f'))
print('can_int_str(\'12334325\'):', can_int_str('12334325'))
print('make_int(\'12334325f\'):', make_int('12334325f'))
print('make_int(\'12334325\'):', make_int('12334325'))
