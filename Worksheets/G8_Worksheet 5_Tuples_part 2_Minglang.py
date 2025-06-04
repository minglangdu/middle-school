"""
Worksheet # 5: Tuples
Student Code
Python Level 3

Name: Minglang Du
Section: 8-D14
"""

# Uncomment any provided print statements as needed to verify results.


"""
Part 2
"""

print('\n *** Problem 6 - Tuple Concatenation *** \n')

# Each class in a school's 8th grade (“8A”, “8B”, “8C”) forms teams for a
# science competition. Class “8A” has formed two teams (“Neutrons”, “Protons”),
# class “8B” has formed two teams (“Electrons”, “Photons”), and class “8C” has
# formed two teams (“Quarks” and “Leptons”).

# To track this information, declare variables teams_8A, teams_8B, and teams_8C
# and assign each to a tuple containing the class and team names. Then, write
# code to combine these tuples into a single tuple called all_teams.

teams_8A = ('8A', 'Neutrons', 'Protons')
teams_8B = ('8B', 'Electrons', 'Photons')
teams_8C = ('8C', 'Quarks', 'Leptons')
all_teams = teams_8A + teams_8B + teams_8C
print(all_teams)


print('\n *** Problem 7 - Tuple Repetition *** \n')

# Each round of the science competition has the same order of subjects for its
# questions: (“Physics”, “Chemistry”, “Biology”, “Astronomy”, “Geology”). There
# are four rounds in the contest. Create a new tuple based on the one below to
# create a continuous subject pattern for the questions in all four rounds.
# Assign the tuple into all_questions.

round_questions = ('Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology')

all_questions = round_questions * 4

print(all_questions)

print('\n *** Problem 8 - Membership Checking *** ')

# 8a. You have a tuple with the collection of books below. Write code to check
#     whether “Hunger Games” is in this collection.

print('\n(8-a)')
books = ('Harry Potter', 'Lord of the Rings', 
         'Hunger Games', 'Percy Jackson', 'Narnia')

print('Hunger Games' in books)

# 8b. Given the same collection of books in the previous question, write a
#     program that checks if “Maze Runner” is not in the collection.

print('\n(8-b)')

print('Maze Runner' in books)

print('\n *** Problem 9 - Tuple Iteration *** ')

# 9a. Using the books tuple, write a loop that prints each book title on a 
#     new line.

print('\n(9-a)')

# 9b. Now, let’s assume the books tuple represents the books’ arrangement on a
#     shelf. Write a for loop that prints the index and title of each book in
#     the books tuple (e.g., “Book 1: Harry Potter”) on a new line.

for i in range(len(books)):
    print(f"Book {i + 1}: {books[i]}")

print('\n(9-b)')

# 9c. Your school is hosting a trivia competition and you’ve been asked to help
#     keep track of the teams and their scores. The data is stored as a tuple
#     (given below), where each element is another tuple that contains a team’s
#     name and their score.

scores = (("Eagles", 150), ("Falcons", 165),
          ("Cardinals", 140), ("Blue Jays", 170))

# Write code to print out each team’s name and their corresponding score on a
# new line, as shown below:
#
#     The team Eagles has a score of 150.
#     The team Falcons has a score of 165. ...etc

for i in range(len(scores)):
    print(f"The team {scores[i][0]} has a score of {scores[i][1]}.")

print('\n(9-c)')


"""
Part 2: Challenge Problems
"""
print('\n *** Problem 10 - Nested Tuple Conversion *** \n')

# Python's built-in tuple() function accepts another data structure such as a
# list as an argument and converts it to a tuple, if it can. However, it only
# converts the outermost layer of the data structure; a list of lists would
# just be converted into a tuple of lists. Try this in the interactive Shell:
#     tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Write a function nested_list_to_tuple() that accepts a list of lists, where 
# each inner list should be converted to a tuple using the tuple() function.
# Your function should return a list of these tuples.

def nested_list_to_tuple(tup):
    ans = []
    for i in tup:
        ans.append(tuple(i))
    return tuple(ans)

print(nested_list_to_tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print('\n *** Problem 11 - Nested Tuple Iteration *** \n')

# You are given a tuple that contains weather data for a week. Each element
# in the tuple is another tuple with two elements: the first is the day of the
# week and the second is that day's average temperature in Fahrenheit.

# Write a function hottest_day(data) to accept that tuple of day-temp tuples
# and find the day with the highest average temperature. It should return a
# tuple consisting of that day and its temperature.

weather_data = (("Monday", 85), ("Tuesday", 80), ("Wednesday", 90),
                ("Thursday", 88), ("Friday", 83),
                ("Saturday", 79), ("Sunday", 85))

def hottest_day(data):
    ans = 0
    for i in range(len(data)):
        if data[i][1] > data[ans][1]:
            ans = i
    return data[ans]

print(hottest_day(weather_data))

#print(hottest_day(weather_data))
# Output: ('Wednesday', 90)


print('\n *** Problem 12 - Tuple Reversal *** \n')

# Write a Python function reverse_tuple() that takes a tuple as its argument 
# and returns a new tuple that is the reverse of the input. Note: tuples may 
# be immutable, but you can form new tuples by slicing existing ones or 
# combining them using concatenation (+). Test your function on tuple_n:

tuple_n = (1, 2, 3, 4, 5)
print("tuple_n =", tuple_n, "\n")

def reverse_tuple(tup):
    a = []
    for i in range(len(tuple_n) - 1, -1, -1):
        a.append(tuple_n[i])
    return tuple(a)
        
print("reversed =", reverse_tuple(tuple_n), "\n")
