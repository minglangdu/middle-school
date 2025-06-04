"""
Worksheet # 2: Python Review
Student Code
Python Level 3

Name:
Section:
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.


"""
Part 2
"""

print('\n *** Problem 7 *** ')

# Given the list of movies below, where the order of the movies
# represents a child’s rankings, write Python code that asks for
# a movie title and prints that movie’s rank (1 being the highest
# and 5 being the lowest) with an informative message. Make sure
# to check for membership first to avoid an error.

movies = ["Toy Story", "Frozen", "The Incredibles",
          "Finding Nemo", "Moana"]

def findmovie(movie):
    ind = movies.index(movie)
    if (ind < 0):
        print("Movie not found")
    else:
        print("Movie is in rank " + str(ind + 1) + "!")
findmovie("Toy Story")
findmovie("Finding Nemo")


print('\n *** Problem 8 *** ')

# Given a list of weekly temperatures below, write Python code that
# asks for a day number (1-7), checks whether it’s within the list’s
# bounds, and prints the temperature for that day if it exists or a
# suitable error message otherwise.

temperatures = [74, 70, 72, 75, 79, 82, 81]

def gettemp(day):
    if (day <= 0 or day > 7):
        print("Invalid day.")
        return
    tem = temperatures[day - 1]
    print("Temperature is " + str(tem) + " Fahrenheit!")

gettemp(1)
gettemp(5)


print('\n *** Problem 9 *** ')

# Given a list of students, write Python code that iterates over the
# list and adds "is awesome!" to each name before printing it out.
# For example, the program should print:
#     Ana is awesome!
#     Bob is awesome!
#     etc.

students = ["Ana", "Bob", "Cid", "Dal", "Eva"]

for student in students:
    print(student, "is awesome!")

print('\n *** Problem 10 *** ')

# Given the two-dimensional list below representing the seats in a
# theater, where "X" means the seat is taken and "O" means the seat
# is available, write code that counts and prints the total number
# of available seats.

seats = [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'O']]
ans = 0
for row in seats:
    for col in row:
        if (col == 'O'):
            ans += 1
print(str(ans), "seats are available.")


"""
Part 2: Challenge Problems
"""

print('\n *** Problem 11 *** ')

# Given the two lists below, one with students’ names and one with 
# their test scores, write code that iterates over both lists
# simultaneously, using index-based iteration, and prints each
# student’s name along with their score. Do this in only two
# additional lines of code after the initial list assignments.

students = ["Ana", "Bob", "Cid", "Dal", "Eva"]
scores = [87, 84, 93, 85, 92]

for i in range(len(students)):
    print("The score of", students[i], "is", str(scores[i]) + ".")
    

print('\n *** Problem 12 *** ')

# The following code is supposed to add up the elements in each row
# of the multiplication table and append the sum to a new list
# called row_sums. However, the program contains two bugs that
# causes some semantic errors. Fix the bugs. Hint: Trace the events
# to see if every action is happening at the correct time, both
# inside and outside the loop.

# Uncomment and fix the buggy code below:

mult_table = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
row_sums = []
row_num = 0
sum_of_row = 0  # The row sum is only initialized to 0 at the start;
                # it should be reset back to 0 for every row

for row in mult_table:
    row_num = row_num + 1
    sum_of_row = 0
    for num in row:
        sum_of_row = sum_of_row + num
    row_sums.append(sum_of_row) # The current row sum is being
                                # appended for every *value*;
                                # should be for every row
        
print("The list of row sums is", row_sums)



