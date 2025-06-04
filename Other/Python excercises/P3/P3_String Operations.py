# EXTREME CRINGE WARNING

# Minglang 6-B1

name2 = "Bob the Builder" # used multiple times
name1 = "Logan" # used multiple times 
supers = "super " * 5 # word repeated multiple times
oscarwildequote = '"Some cause happiness wherever they go; others whenever they go."'
# long quote
grammaticallyincorrectmodifiers = "bestest of " * 3 # word repeated multiple times
endsentences = (f"Right, {name1}?! ") * 3 # word repeated multiple times

chat1 = f"Good morning {name1}!"
chat2 = f"My name is {name2}!"
chat3 = f"I'm {supers}excited to get to know you!\n"
chat4 = f"I'm sure we'll be {grammaticallyincorrectmodifiers}friends!"
chat5 = f'You know, Oscar Wilde once famously wrote, {oscarwildequote}'
chat6 = "I bet you can tell I'm one of the former!"

print(chat1)
print(chat2)
print(chat3, end = "")
print(chat4)
print(chat5)
print(chat6)
print(endsentences)

# output:

"""
Good morning Logan!
My name is Bob the Builder!
I'm super super super super super excited to get to know you!
I'm sure we'll be bestest of bestest of bestest of friends!
You know, Oscar Wilde once famously wrote, "Some cause happiness wherever they go; others whenever they go."
I bet you can tell I'm one of the former!
Right, Logan?! Right, Logan?! Right, Logan?! 
"""