# Minglang Du
# November 3, 2022
# Project 2: Variables, Expressions, and Script Mode

# 1: Volume of sphere = 523.3333333333334 inches^3

r = 5
# calculate sphere volume using formula
sphere_volume = (4/3) * 3.14 * (r ** 3)
print("problem 1: The sphere's volume is " + str(sphere_volume) + " inches^3") # print

# 2: Total cost = $945.4499999999999

price = 24.95
# apply 40% discount
price -= price * (40 / 100)
# calculate price for buying
# book sixty times
price *= 60
# add shipping fee
price += 3
price += (0.75 * (60 - 1))
print("problem 2: the total cost for the 60 books is $" + str(price)) # print

# 3: Truckloads = 21 truckloads

volume = 42 * 27 * 10
# divide volume by truck capacity
# to find amount of truckloads
truckloads = volume / 540
print("problem 3: I need to excavate " + str(truckloads) + " truckloads of dirt") # print

# 4: money_saved = $4.799999999999983

# find costs if you buy
# in packages of 6 and 4
packages_6 = (24 / 6) * 17.10
packages_4 = (24 / 4) * 12.20
saved = packages_4 - packages_6 # find difference
print("problem 4: Choosing 6 packages over 4 packages saves $" + str(saved)) # print
# 5: perimeter = 101.43819034784589 cm

leg_1 = 35
# modify area formula for
# triangle to get leg2
leg_2 = (420 / leg_1) * 2
# use pythagorean formula to find hypotenuse
hypotenuse = (leg_1 ** 2 + leg_2 ** 2) ** (1/2)
# add up
perimeter = leg_1 + leg_2 + hypotenuse
print("problem 5: The perimeter of the right triangle is " + str(perimeter) + " cm") # print

# 6: area_of_face = 899.9999999999995 cm^2

new_volume = 216000
# find old volume by dividing each dimension by 2
old_volume = new_volume / (2 ** 3)
# cube root old volume
old_edge_length = old_volume ** (1/3)
# square old edge length
old_face_area = old_edge_length ** 2
print("problem 6: The area of the face of the original cube is " + str(old_face_area) + " cm^2") # print

# 7: rate = 3000.0 millimeters / second

base = 50
fill_rate = 15 * 1000 # get the fill rate in cm^3
# find rate
rate = ((fill_rate / base) / 60) * 10
# divide it by sixty and multiply by 10
# to convert from minutes to seconds and
# centimeters to millimeters
print("problem 7: The rate at which the height of the water tank increases is " + str(rate) + " millimeters / second") # print