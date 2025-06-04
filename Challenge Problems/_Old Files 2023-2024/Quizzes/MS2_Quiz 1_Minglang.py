"""
Quiz #1: Chapter 7
Problem Code for Students
Python Level 2

Student Name: Minglang
Section: C6
"""

"""
Problem 1
"""

print('\n*** Problem 1 ***\n')

# Remove the triple-single quotes above and below the code.
# Fill in the missing code and test to verify it works.
# In the incomplete formula below, G is 6.673*10**-11. Refer
# to the hardcopy quiz paper for the rest of the formula.


def accel_grav(M, R):
    acc_g = (6.673*10**-11 * M) / R**2         # Complete this line of code
    return acc_g
    
earth_g = accel_grav(5.97*10**24, 6371000)

# For testing purposes only:
print('Acceleration due to gravity on Earth = about',
      round(earth_g, 1), 'meters per second, per second')



"""
Problem 2
"""

# Remove the triple-single quotes above and below the code.
# Complete the function vel_fall() and test it by completing the
# call to vel_fall() with the given stats for planet X. Refer to
# the quiz paper for details.

print('\n*** Problem 2 ***\n')


# t is time
# g is acceleration due to gravity (calculated
#      by calling accel_grav)
# v is velocity

def vel_fall(t, g): 
    # Complete this function by calculating the downward velocity
    # of a falling object given the time it has been falling (in
    # seconds) and the planet's acceleration due to gravity. Return
    # the velocity. See the quiz paper for the formula.
    vel = t * g
    return vel

vf_earth = vel_fall( 3, accel_grav(5.97*10**24, 6371000) )

# Fill in the function call below. Use a time of 3 seconds.
# For the call to accel_grav, use:
# M (planet mass) = 5.97 * 10**24 kg
# R (planet radius) = 10000 m
vf_planetx = vel_fall( 3, accel_grav(5.97 * 10**24, 10000) )  

# For testing purposes only:
print('Velocity after falling for 3 seconds on Earth = about',
      round(vf_earth, 1), 'meters per second')
print('Velocity after falling for 3 seconds on Planet X = about',
      round(vf_planetx, 1), 'meters per second')


"""
Problem 3
"""

# Remove the triple-single quotes above and below the code.
# Fill in the missing code and test to verify it works.

print('\n*** Problem 3 ***\n')


           #a - assign count to 11
count = 11

def countdown():
                #b - grant countdown() access to count
    global count
                #c - update count, decreasing it by 1
    count -= 1
    print(count, '...')

for i in range(10):
    countdown()

"""
Problem 4
"""

# Remove the triple-single quotes above and below the code.
# Fill in the missing code and test to verify it works.

print('\n*** Problem 4 ***\n')


def hr_min_sec(total_seconds):
    # Divide total number of seconds by 3600 seconds per hour to
    # get the number of hours (use integer divison // to get a 
    # whole number of hours):
    hours = total_seconds // 3600
    
    # To get the total number of minutes, divide total seconds by 
    # 60 seconds per minute (using //). But that number also 
    # includes minutes that were already grouped and counted as
    # whole hours. So, after the // 60 operation, you must exclude
    # the minutes that were already counted as hours. Do this by 
    # getting the *remainder* of dividing the total minutes by 60
    # minutes per hour. That remainder equals the leftover minutes 
    # after you've counted the hours. The modulo (%) operator can 
    # calculate remainders (e.g., the remainder of X divided by Y
    # is X % Y).
    minutes = total_seconds // 60 % 60
    
    # Finally, to get the number of seconds left once you've
    # assigned seconds to whole hours and minutes, just get the
    # remainder of dividing total seconds by 60 seconds per minute:
    seconds = total_seconds % 60

    # Write a print statement to output the total seconds and the
    # converted hours, minutes, and seconds with labels. For
    # example: 21209 seconds = 5 hours, 53 minutes, and 29 seconds
    print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, and {seconds} seconds")

hr_min_sec(20000)



"""
Problem 5
"""

# Remove the triple-single quotes above and below the code to
# run the code. Then, fix the error and test again.

print('\n*** Problem 5 ***\n')


def print_label(value, label):
    print(str(value), label)

print_label(35.5, 'meters')


"""
Problem 6
"""

# Remove the triple-single quotes above and below the code to
# run the code. Then, fix the error and test again.

print('\n*** Problem 6 ***\n')


def print_together(str1, str2):
    print(str(str1) + str(str2))

price = 15.95
print_together('$', price)



"""
Problem 7
"""

# Remove the triple-single quotes above and below the code to
# run the code. Then, fix the error and test again.

print('\n*** Problem 7 ***\n')


sales_tax = 0.085
items_cost = 250
cost_with_tax = items_cost + items_cost * sales_tax
print('Your subtotal for your items is $', items_cost, sep='')
print('Including tax, your total comes out to $', cost_with_tax, sep='')
