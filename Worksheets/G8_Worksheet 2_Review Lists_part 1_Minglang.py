"""
Worksheet # 2: Python Review
Student Code
Python Level 3

Name: Minglang Du 
Section: 8-D14
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n *** Problem 1 *** ')

# Given a list num_list = [5, 7, 9, 11, 13], write a statement
# to create a new list containing the second, third, and fourth
# elements from the original list:

num_list = [5, 7, 9, 11, 13]
new_num_list = [num_list[1], num_list[2], num_list[3]]
print(new_num_list)


print('\n *** Problem 2 *** ')

# Write a Python function copy_and_add() that takes a list and
# an element as parameters, makes a copy of the list, adds the
# element to the end of the copied list, and returns the copy.
# Write your own test cases.

def copy_and_add(list, ele):
    copy = list[:]
    copy.append(ele)
    return copy
print(copy_and_add([1, 2], 3))
print(copy_and_add([2, 2, 2], 4))


print('\n *** Problems 3 and 4 *** ')

# Write a function first_and_last(input_list) that takes a list as
# a parameter and returns a new list containing only the first and 
# the last elements of the input list. For example, for the input 
# list [1, 2, 3, 4, 5], the function should return [1, 5].

def first_and_last(list):
    return [list[0], list[-1]]
def fandl(list):
    del list[1:-1]
    return list
def fandl2(list):
    a = []
    a.append(list[0])
    a.append(list[-1])
    return a

print(first_and_last([1, 2, 3, 4, 5]))
print(fandl([3, 2, 3, 4, 5]))
print(fandl2([1, 2, 3, 4, 9]))


"""
Part 1: Challenge Problems
"""

print('\n *** Problem 5 *** ')

# Write a function merge_list_halves(list1, list2) that takes the
# first half of its parameter list1 (rounded down for odd-length
# lists) and the second half of list2 (rounded up for odd-length 
# lists), combines the two halves into a new list, and returns it.
# Create at least test two test cases: one with even-length lists,
# and one with odd-length lists.

import math

def merge_list_halves(list1, list2):
    pivot1 = math.floor(len(list1) / 2)
    pivot2 = math.floor(len(list2) / 2)
    list1 = list1[:pivot1]
    list1.extend(list2[pivot2:])
    return list1

print(merge_list_halves([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(merge_list_halves([1, 2, 3, 4], [5, 6, 7, 8]))


print('\n *** Problem 6 *** ')

# Write a function called interleave_list_halves(values) to combine the first
# half of list1 with the second half of list2, like merge_list_halves() from
# #5, but with one key difference—it should interleave the two halves. That
# means, the function should take one element from the first half of list1,
# then one from the second half of list2, and so on, repeating this pattern
# until it has used up all elements from one or both halves. If one half runs
# out of elements before the other, append all remaining elements from the
# other half to the end of the new list.

def interleave_list_halves(list1, list2):
    pivot1 = math.floor(len(list1) / 2)
    pivot2 = math.floor(len(list2) / 2)
    list1 = list1[:pivot1]
    list2 = list2[pivot2:]
    p1 = 0
    p2 = 0
    ans = []
    while (p1 < len(list1) and p2 < len(list2)):
        ans.append(list1[p1])
        ans.append(list2[p2])
        p1 += 1
        p2 += 1
    while (p1 < len(list1)):
        ans.append(list1[p1])
        p1 += 1
    while (p2 < len(list2)):
        ans.append(list2[p2])
        p2 += 1
    return ans

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [9, 10, 11]
print(interleave_list_halves(list1, list2))



