"""
Worksheet # 6: Dictionaries
Student Code
Python Level 3

Name: Minglang
Section: 8-D14
"""

class_students = {'John': 12, 'Alex': 14}

# 2c. Create another dictionary named new_students with the following keys and
#     values: 'Michael': 14, 'Sarah': 13. Print it.

print('\n(2-c)')

new_students = dict(Michael=14,Sarah=13)
print(new_students)
# 2d. Merge new_students into the class_students dictionary using the update()
#     method and print both new_students and the updated class_students.

print('\n(2-d)')

class_students.update(new_students)
print(new_students, class_students)

# 2e. Clear all entries in the class_students dictionary using the clear()
#     method and print the updated dictionary.

print('\n(2-e)')

class_students.clear()
print(class_students)

print('\n *** Problem 3 - Dictionary View Objects *** ')

# You are given the following dictionary:
fruit_colors = {'Apple': 'Red', 'Banana': 'Yellow', 'Grapes': 'Purple'}

# 3a. Get a view object of all keys in fruit_colors and print it.

print('\n(3-a)')

k = fruit_colors.keys()
print(k)

# 3b. Get a view object of all values in fruit_colors and print it.

print('\n(3-b)')

v = fruit_colors.values()
print(v)

# 3c. Get a view object of all items (key-value pairs) in fruit_colors and
#     print it.

print('\n(3-c)')

i = fruit_colors.items()
print(i)

# 3d. Add a new key-value pair 'Orange': 'Orange' to fruit_colors and print
#     the updated view objects of keys, values, and items.

print('\n(3-d)')

fruit_colors['Orange'] = 'Orange'
print(k, v, i)

# 3e. Check if 'Apple' is in the keys of fruit_colors using a view object.

print('\n(3-e)')

print(f"Apple is {'not ' if 'Apple' not in fruit_colors.keys() else ''}in fruit_colors.keys().")

# 3f. Check if 'Green' is in the values of fruit_colors using a view object.

print('\n(3-f)')

print(f"Green is {'not ' if 'Green' not in fruit_colors.values() else ''}in fruit_colors.values().")

# 3g. Check if the key-value pair ('Banana', 'Yellow') is present in
#     fruit_colors using a view object.

print('\n(3-g)')

print(f"""('Banana', 'Yellow') is {'not ' if ('Banana', 'Yellow') not
in fruit_colors.items() else ''}in fruit_colors.items().""")

"""
Challenge Problem
"""

print('\n *** Problem 4 - Dictionary View Objects *** ')

# 4a. Convert the view object of keys in fruit_colors to a list and remove
#     'Apple' from the list. Print the updated list and also check if 'Apple'
#     still exists in the fruit_colors dictionary.



print('\n(4-a)')
# 4b. Create a function that takes a dictionary and a color as arguments. This
#     function should return all fruits (keys) that have this color, utilizing
#     a view object of the dictionary.

k = list(k)
k.remove('Apple')
print(k, 'Apple' in fruit_colors)

print('\n(4-b)')

def get_fruits_of_color(d, col):
    ans = []
    for i in d.items():
        if col in i[1]:
            ans.append(i[0])
    return ans

print(get_fruits_of_color(fruit_colors, 'Red'))  # Output: ['Apple']