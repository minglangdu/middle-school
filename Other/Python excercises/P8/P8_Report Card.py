"""
Project #8: Report Card

Name: Minglang
Date: 5/8/2023
Class: 6-B1
"""

# ask_pt_grade() asks the user to enter a percentage grade
# and returns the result.
def ask_pt_grade(subject):
    pt_grade = float(input(f'Please enter your {subject.lower()} percentage grade: '))
    return pt_grade

# pt_grade_to_letter() converts a percentage grade to a letter grade.
# It accepts a percentage grade as an argument and uses conditionals
# to determine the equivalent letter grade and then returns that.
def pt_grade_to_letter(pt_grade):    
    if pt_grade > 94:
        ltr_grade = 'A'
    elif 90 <= pt_grade < 94:
        ltr_grade = 'A-'
    elif 87 <= pt_grade < 90:
        ltr_grade = 'B+'
    elif 83 <= pt_grade < 87:
        ltr_grade = 'B'
    elif 80 <= pt_grade < 83:
        ltr_grade = 'B-'
    elif 77 <= pt_grade < 80:
        ltr_grade = 'C+'
    elif 73 <= pt_grade < 77:
        ltr_grade = 'C'
    elif 70 <= pt_grade < 73:
        ltr_grade = 'C-'
    elif 60 <= pt_grade < 69:
        ltr_grade = 'D'
    else:
        ltr_grade = 'F'            
    return ltr_grade

# grade_point() converts a letter grade to a grade point.
# It accepts a letter grade as an argument and uses conditionals
# to determine the equivalent grade point and then returns that.
def grade_point(ltr_grade):
    if ltr_grade == 'A':
        g_point = 4.0
    elif ltr_grade == 'A-':
        g_point = 3.7
    elif ltr_grade == 'B+':
        g_point = 3.3
    elif ltr_grade == 'B':
        g_point = 3.0
    elif ltr_grade == 'B-':
        g_point = 2.7
    elif ltr_grade == 'C+':
        g_point = 2.3
    elif ltr_grade == 'C':
        g_point = 2.0
    elif ltr_grade == 'C-':
        g_point = 1.7
    elif ltr_grade == 'D':
        g_point = 1.0
    else:
        g_point = 0.0
    return g_point

# greet user
print("Welcome to the Interactive Report Card program!\n")
# Get student name and print instructions
student_name = input("Please enter the student name: ")
print("When inputting grades, input them out of 100 and do not use a '%' sign.")
# map of subjects and empty lists representing lists
subjects = {'Metalsmithing':[], 'Masonry':[], 'Carpentry':[], 'Jewelry':[], 'Cheesemaking':[], 'Sun Staring':[]}
s = 0 # sum of grade points
for subject in subjects.keys(): # ask for percentage grades and store as grade points and letter grades
    percent_grade = ask_pt_grade(subject)
    subjects[subject].append(pt_grade_to_letter(percent_grade))
    subjects[subject].append(str(grade_point(subjects[subject][0])))
    s += float(subjects[subject][1])
# start report card
print('\n' + '-' * 35 + '\n' + 'Report Card for ' + student_name.title() + '\n' + '-' * 35)
for subject in subjects.keys(): # print report card (letter grades)
    print(subject + ' ' * (20 - len(subject)) + subjects[subject][0] + ' ' * (10 - len(subjects[subject][0])) + subjects[subject][1])
print('-' * 35 + '\n' + 'GPA' + ' ' * 17 + '--' + ' ' * 8 + str(round(s / len(subjects), 2))) # print gpa
print('\n' + f'Thank you for using this Interactive Report Card program, {student_name.title()}!')
# print end message

# output 1
"""
Welcome to the Interactive Report Card program!

Please enter the student name: Urist
When inputting grades, input them out of 100 and do not use a '%' sign.
Please enter your metalsmithing percentage grade: 59
Please enter your masonry percentage grade: 60
Please enter your carpentry percentage grade: 72
Please enter your jewelry percentage grade: 76
Please enter your cheesemaking percentage grade: 79
Please enter your sun staring percentage grade: 81

-----------------------------------
Report Card for Urist
-----------------------------------
Metalsmithing       F         0.0
Masonry             D         1.0
Carpentry           C-        1.7
Jewelry             C         2.0
Cheesemaking        C+        2.3
Sun Staring         B-        2.7
-----------------------------------
GPA                 --        1.62

Thank you for using this Interactive Report Card program, Urist!
"""
# output 2
"""
Welcome to the Interactive Report Card program!

Please enter the student name: Urist the second
When inputting grades, input them out of 100 and do not use a '%' sign.
Please enter your metalsmithing percentage grade: 86
Please enter your masonry percentage grade: 89
Please enter your carpentry percentage grade: 93
Please enter your jewelry percentage grade: 100
Please enter your cheesemaking percentage grade: 0
Please enter your sun staring percentage grade: 96.9

-----------------------------------
Report Card for Urist The Second
-----------------------------------
Metalsmithing       B         3.0
Masonry             B+        3.3
Carpentry           A-        3.7
Jewelry             A         4.0
Cheesemaking        F         0.0
Sun Staring         A         4.0
-----------------------------------
GPA                 --        3.0

Thank you for using this Interactive Report Card program, Urist The Second!
"""