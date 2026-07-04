"""
===============================================================
            SOFTWARE TRAINING COURSE - DAY 01
---------------------------------------------------------------
Author      : Anju Sharma
Topic       : Python Interview MCQs & Practice Programs
Description : This file contains Python interview-based
              questions and practice programs discussed
              during Day 1 of the Software Training Course.
===============================================================
"""

print("=" * 65)
print("DAY 01 - PYTHON INTERVIEW MCQs & PRACTICE")
print("=" * 65)


# ===============================================================
# Q1. Print Alternate Elements Using List Slicing
# ===============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntax:
# list[start : stop : step]

print(numbers[::2])

# Output:
# [1, 3, 5, 7, 9]

# Interview Note:
# Step value 2 prints every alternate element.


print("\n" + "*" * 60)


# ===============================================================
# Q2. Replace Alternate Elements Using List Slicing
# ===============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replace alternate elements
numbers[::2] = [10, 20, 30, 40, 50]

print(numbers)

# Output:
# [10, 2, 20, 4, 30, 6, 40, 8, 50]

# Important:
# Number of replacement values must match the selected slice.


print("\n" + "*" * 60)


# ===============================================================
# Q3. Reverse a Portion of a List
# ===============================================================

numbers = [1, 2, 3, 4, 5]

print(numbers[3:0:-1])

# Output:
# [4, 3, 2]

# Explanation:
# Start index = 3
# Stop index = 0 (excluded)
# Step = -1


print("\n" + "*" * 60)


# ===============================================================
# Q4. Remove Last Element From Each Row (Using pop())
# ===============================================================

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for row in matrix:
    print(row.pop())

# Output:
# 4
# 7
# 11
# 15

# Interview Note:
# pop() removes and returns the last element.


print("\n" + "*" * 60)


# ===============================================================
# Q5. Mutable Default Argument (Very Important Interview MCQ)
# ===============================================================

def add_value(value, values=[]):
    """
    Default mutable arguments are created only once.
    Therefore, the same list is reused in every function call.
    """

    values.append(value)
    print(values)


add_value(1)
add_value(2)
add_value(3)

# Output:
# [1]
# [1, 2]
# [1, 2, 3]

# Interview Note:
# Mutable default arguments retain their values
# between function calls.


print("\n" + "*" * 60)


# ===============================================================
# Q6. Left Shift Elements of a List
# ===============================================================

numbers = [1, 2, 3, 4, 5, 6]

for i in range(1, len(numbers)):
    numbers[i - 1] = numbers[i]

for num in numbers:
    print(num, end=" ")

# Output:
# 2 3 4 5 6 6

# Explanation:
# Every element shifts one position to the left.
# The last value remains unchanged.


print("\n\n" + "*" * 60)


# ===============================================================
# Q7. Find Maximum Element in a 2D List
# ===============================================================

data = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]


def find_max(matrix):

    maximum = matrix[0][0]

    for row in matrix:
        for element in row:
            if element > maximum:
                maximum = element

    return maximum


print(find_max(data))

# Correct Output:
# 8

# Correction:
# In your code, return was inside the loop,
# so the function stopped after checking only one row.


print("\n" + "*" * 60)


# ===============================================================
# Q8. Difference Between Assignment and Copy
# ===============================================================

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']

# Reference Copy
fruit_list2 = fruit_list1

# Shallow Copy
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

total = 0

for fruit in (fruit_list1, fruit_list2, fruit_list3):

    if fruit[0] == 'Guava':
        total += 1

    if fruit[1] == 'Kiwi':
        total += 20

print(total)

# Output:
# 22

# Interview Note:
# '=' creates a reference.
# [:] creates a shallow copy.


print("\n" + "*" * 60)


# ===============================================================
# Q9. zip() Function
# ===============================================================

for i, j in zip(range(1, 6), range(5, 0, -1)):

    if i == 3 and j == 3:
        continue

    print(i, j)

# Output:
# 1 5
# 2 4
# 4 2
# 5 1

# Interview Note:
# zip() combines multiple iterables.


print("\n" + "*" * 60)


# ===============================================================
# Q10. Empty Tuple Special Method
# ===============================================================

empty_tuple = ()

# Uncomment to observe the error
# print(empty_tuple.__len__())

# Original code:
# print(init_tuple.__le__())

# Interview Note:
# __le__() expects another object for comparison.
# Calling it without an argument raises TypeError.

print("Q10 is an interview theory question.")

# ===============================================================
# Q11. Compare Two Tuples
# ===============================================================

tuple_a = ('a', 'b')
tuple_b = ('a', 'b')

print(tuple_a == tuple_b)

# Output:
# True

# Interview Note:
# Parentheses are optional while creating tuples.
# ('a','b') and 'a','b' are exactly the same.


print("\n" + "=" * 60)


# ===============================================================
# Q12. Tuple Multiplication (Interview MCQ)
# ===============================================================

numbers = [1, 2, 3]

result = ('Python',) * (numbers.__len__() - numbers[::-1][0])

print(result)

# Output:
# ()

# Explanation:
# numbers.__len__() = 3
# numbers[::-1][0] = 3
# 3 - 3 = 0
# Tuple multiplied by 0 becomes an empty tuple.


print("\n" + "=" * 60)


# ===============================================================
# Q13. Single Element Tuple (Interview MCQ)
# ===============================================================

single_value = ('Python')

print(type(single_value))

# Output:
# <class 'str'>

# Interview Note:
# This is NOT a tuple.

# Correct way:
single_tuple = ('Python',)

print(type(single_tuple))

# Output:
# <class 'tuple'>


print("\n" + "=" * 60)


# ===============================================================
# Q14. Dictionary with Tuple Keys
# ===============================================================

student_data = {
    (1, 2): 1,
    (2, 3): 2,
    (4, 5): 3
}

print(student_data[(4, 5)])

# Output:
# 3

# Interview Note:
# Tuples are immutable, so they can be used as dictionary keys.


print("\n" + "=" * 60)


# ===============================================================
# Q15. Invalid Dictionary Access
# ===============================================================

student = {
    'a': 1,
    'b': 2,
    'c': 3
}

# print(student['a', 'b'])

# Output:
# KeyError

# Explanation:
# ('a','b') is treated as a single tuple key.
# Such a key doesn't exist in the dictionary.


print("\n" + "=" * 60)


# ===============================================================
# Q16. Count Dictionary Keys
# ===============================================================

fruits = {}


def add_one(item):
    """Adds an item to the dictionary."""

    if item in fruits:
        fruits[item] += 1
    else:
        fruits[item] = 1


add_one("Apple")
add_one("Bpple")
add_one("apple")

print(len(fruits))

# Output:
# 3

# Interview Note:
# Dictionary keys are case-sensitive.
# "Apple" and "apple" are different keys.


print("\n" + "=" * 60)


# ===============================================================
# Q17. Integer Key vs String Key
# ===============================================================

data = {}

data[1] = 1
data['1'] = 2
data[1] += 1

total = 0

for key in data:
    total += data[key]

print(total)

# Output:
# 4

# Explanation:
# 1 and '1' are different dictionary keys.


print("\n" + "=" * 60)


# ===============================================================
# Q18. Integer Key vs Float Key
# ===============================================================

my_dict = {}

my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

print(my_dict)

total = 0

for key in my_dict:
    total += my_dict[key]

print(total)

# Output:
# {1: 4, '1': 2}
# 6

# Interview Note:
# 1 == 1.0
# Therefore 1.0 replaces the value of key 1.


print("\n" + "=" * 60)


# ===============================================================
# Q19. Tuple as Dictionary Keys
# ===============================================================

my_dict = {}

my_dict[(1, 2.4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

total = 0

for key in my_dict:
    total += my_dict[key]

print(total)
print(my_dict)

# Output:
# 30
# {(1, 2.4): 8, (4, 2, 1): 10, (1, 2): 12}

# Interview Note:
# Immutable tuples can be dictionary keys.


print("\n" + "=" * 60)


# ===============================================================
# Q20. Nested Dictionary (Interview MCQ)
# ===============================================================

box = {}
jars = {}
crates = {}

box['biscuit'] = 1
box['cake'] = 3

jars['jam'] = 4

crates['box'] = box
crates['jars'] = jars

# print(len(crates[box]))

# Output:
# TypeError

# Correct Access:
print(len(crates['box']))

# Output:
# 2

# Explanation:
# Dictionary keys should be accessed using strings.
# box is a dictionary object, not a valid key in crates.

# ===============================================================
# Q21. Dictionary Sorting and Memory Addressing
# ===============================================================

# Dictionary Example
student_marks = {
    'c': 97,
    'a': 96,
    'b': 98
}

# sorted() returns the keys in ascending order.
for key in sorted(student_marks):
    print(student_marks[key])

# Output:
# 96
# 98
# 97

# Interview Note:
# sorted(dictionary) sorts only the keys.


print("\n" + "=" * 60)


# ===============================================================
# Memory Addressing using id()
# ===============================================================

math = 50
chemistry = 50
physics = 50

print(id(math))
print(id(chemistry))
print(id(physics))

# Interview Note:
# Small integers are cached by Python.
# Therefore, all three variables may have the same memory address.


print("\n" + "=" * 60)


# ===============================================================
# Q22. Dictionary copy()
# ===============================================================

record = {
    "Name": "Python",
    "Age": "20"
}

copied_record = record.copy()

print(id(copied_record) == id(record))
print(id(copied_record))
print(id(record))

# Output:
# False

# Interview Note:
# copy() creates a new dictionary.
# Both dictionaries have different memory addresses.


print("\n" + "=" * 60)


# ===============================================================
# Q23. Delete and Recreate Dictionary
# ===============================================================

record = {
    "Name": "Python",
    "Age": "20",
    "Address": "NJ",
    "Country": "USA"
}

id1 = id(record)

del record

record = {
    "Name": "Python",
    "Age": "20",
    "Address": "NJ",
    "Country": "USA"
}

id2 = id(record)

print(id1 == id2)

# Interview Note:
# Output may be True or False.
# Python may reuse the memory location after deletion.
# Do not depend on this behaviour in interviews.


print("\n" + "=" * 60)


# ===============================================================
# Type Casting in Python
# ===============================================================

print("Integer Conversion")

print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))

# Invalid Conversions

# print(int(10+5j))
# print(int("4.22"))
# print(int("Anju"))

# Interview Note:
# Complex numbers cannot be converted to int.
# Floating-point strings cannot be converted to int.
# Non-numeric strings raise ValueError.


print("\n" + "=" * 60)


print("Float Conversion")

print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))

# Invalid

# print(float(50+2j))
# print(float("Python"))

# Interview Note:
# Complex numbers cannot be converted into float.


print("\n" + "=" * 60)


print("Boolean Conversion")

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1 + 2j))
print(bool(0 + 0j))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool("Anju"))

# Interview Note:
# Any non-zero number is True.
# Empty values evaluate to False.


print("\n" + "=" * 60)


# ===============================================================
# Q24. Move All Zeros to the End
# ===============================================================

numbers = [0, 1, 0, 3, 12]

for value in numbers[:]:
    if value == 0:
        numbers.remove(value)
        numbers.append(value)

print(numbers)

# Output:
# [1, 3, 12, 0, 0]

# Interview Note:
# Iterate over numbers[:] instead of numbers
# while modifying the list.


print("\n" + "=" * 60)


# ===============================================================
# Q25. Intersection of Three Arrays
# ===============================================================

array1 = [1, 2, 3]
array2 = [2, 3, 4]
array3 = [3, 4, 5]

for number in array1:
    if number in array2 and number in array3:
        print(number)

# Output:
# 3


print("\n" + "=" * 60)


# ===============================================================
# Q26. Maximum Consecutive Ones
# ===============================================================

numbers = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]

count = 0
maximum = 0

for number in numbers:

    if number == 1:
        count += 1
        maximum = max(maximum, count)

    else:
        count = 0

print(maximum)

# Output:
# 4

# Interview Note:
# Frequently asked coding question.


print("\n" + "=" * 60)


# ===============================================================
# Q27. Check Whether a List is Palindrome
# ===============================================================

numbers = [1, 2, 3, 2, 1]

if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome

# Correction:
# Your previous code:
#
# if list[::-1]:
#
# was incorrect because every non-empty list is True.


print("\n" + "=" * 60)


# ===============================================================
# Q28. Reverse a String
# ===============================================================

text = "hello"

print(text[::-1])

# Output:
# olleh


print("\nUsing Loop\n")

text = "hello"

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

print(reverse)

# Output:
# olleh


print("\n" + "=" * 60)


# ===============================================================
# Q29. Remove Duplicate Characters from a String
# ===============================================================

text = "Programming"

result = ""

for character in text:

    if character not in result:
        result += character

print(result)

# Output:
# Progamin

# Interview Note:
# Order of first occurrence is preserved.

# ===============================================================
# Q30. Security Key (Count Repeating Digits)
# ===============================================================

"""
Problem Statement:
A company is transmitting data in the form of numbers.
The security key is defined as the count of distinct digits
that appear more than once in the given data.

If no digit is repeated, print -1.
"""

# Taking input from the user
data = input("Enter the data: ")

security_key = 0

# Check each digit from 0 to 9
for digit in "0123456789":

    # If a digit appears more than once
    if data.count(digit) > 1:
        security_key += 1

# Display the result
if security_key == 0:
    print(-1)
else:
    print(security_key)

# ---------------------------------------------------------------
# Example 1
# Input:
# 12233345
#
# Output:
# 2
#
# Explanation:
# Repeated digits are:
# 2 (appears 2 times)
# 3 (appears 3 times)
#
# Therefore, Security Key = 2
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Example 2
# Input:
# 123456
#
# Output:
# -1
#
# Explanation:
# No digit is repeated.
# ---------------------------------------------------------------

# Interview Note:
# data.count(digit) returns the number of times
# a particular digit occurs in the input string.
#
# Time Complexity : O(10 × n) ≈ O(n)
# Space Complexity: O(1)