"""
Quiz # 1: Python Shortcuts
Student Code
Python Level 3

(For Publications use: Document Code 09-969.154-24)

Fill out your name and section below.

Name: Minglang Du
Section: 8-D14
"""

# 1. Given the variables first_name = "Ada" and last_name = "Lovelace",
#    use f-string formatting to print the full name in the format:
#    "Last, First: Lovelace, Ada". [12 points]

print("\n*** Problem 1 ***")
first_name = "Ada"
last_name = "Lovelace"

print(f"Last, First: {last_name}, {first_name}")

# 2. Given the variables product = "Apple", quantity = 10, and price = 1.2,
#    use f-string formatting to print:
#       "The total price for 10 Apples is $12.00."
#    Don't just print those literal values--print variables and expression(s).
#    [18 points]

print("\n*** Problem 2 ***")
product = "Apple"
quantity = 10
price = 1.2

print(f"""The total price for {quantity} {product}{"s" if quantity > 1 else ""} \
is ${price * 10:.2f}.""")


# 3. Use a from-import statement to import pi from the math module. Then, use
#    f-string formatting to print pi rounded to 4 decimal places. [12 points]

print("\n*** Problem 3 ***")

from math import pi

print(f"{pi:.4f}")

# 4. Use multiple assignment to assign the values True, False, and True to the
#    variables p, q, and r respectively. [18 points]

print("\n*** Problem 4 ***")

p, q, r = True, False, True

print("p is", p, "... q is", q, "... r is", r)   # Uncomment when you are done



# 5. Modify the following code to use augmented assignment for the variable
#    updates. [24 points]

print("\n*** Problem 5 ***")

score = 0
score += 20
score *= 3
score /= 2
score -= 10

print("The final score is", score)  # Output: 20


# 6. Use line continuation to split the following calculation of a cylinder
#    volume over four lines. The calculation must include all the same 
#    terms, including the two function calls, just split over four lines.
#    Ensure the code works and the answer remains the same. [16 points]

print("\n*** Problem 6 ***")

import math

# Given values
circumference = 31.4  # meters
surface_area = 314.16  # square meters
radius = circumference / (2 * math.pi) # meters

# Calculation of cylinder_volume - split this over four lines
cylinder_volume = (math.pi * radius**2 * \
                   (surface_area - 2 * math.pi * radius ** 2) \
                   / (2 * math.pi * radius))

print(round(cylinder_volume, 1), "cubic meters")  # Output: 392.9 cubic meters
