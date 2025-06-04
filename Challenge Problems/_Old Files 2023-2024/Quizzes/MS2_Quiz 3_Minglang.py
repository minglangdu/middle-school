"""
Quiz #3: Chapter 9
Problem Code for Students
Python Level 2
"""

print ('\n *** Problem 1 *** \n')

# Should output the first n multiples of 2
def multiples_of_2(n):
    i = 1
    while i <= n:
        print(i*2)
        i += 1
    
multiples_of_2(5)


print ('\n\n *** Problem 2 *** \n')

# Should count down by 2 from x to 1, then print Blastoff!
def countdown_by_2(x):
    while x >= 0:
        print(x)
        x = x - 2
    print('Blastoff!')
    
countdown_by_2(10)


print ('\n\n *** Problem 3 *** ')

print ('\nUncomment to run')

# age_menu() should ask the user to choose an option from the menu.
# Depending on the choice he inputs, ask for his age in years and
# calculate his age in months, days, or hours.
def age_menu():
    ans = -1
    while ans != 4:
        print('\n << Age Calculator Menu: >>')
        print('1. Calculate your age in months')
        print('2. Calculate your age in days')
        print('3. Calculate your age in hours')
        print('4. Quit')
        ans = input('\nEnter your choice from the menu: ')
        if ans == '1':
            age = int(input('Enter your age in years: '))
            print('You are about', age*12, 'months old.')
        elif ans == '2':
            age = int(input('Enter your age in years: '))
            print('You are about', age*365, 'days old.')
        elif ans == '3':
            age = int(input('Enter your age in years: '))
            print('You are about', age*365*24, 'hours old.')
        elif ans == '4':
            print('Thanks for using the Age Calculator! Goodbye!')
        else:
            print('Invalid input! Please try again.')
    
age_menu()