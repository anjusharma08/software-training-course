# ===============================================================
# Day 04 – Python List & OOP Practice
# ===============================================================

# Topics:
# 1. OOP Practice Questions
# 2. Create Object
# 3. Constructor (__init__)
# 4. Method Creation
# 5. Method Overriding
# 6. Static Method
# 7. Python List
# 8. List Indexing
# 9. List Slicing
# 10. List Modification
# 11. Membership Operator
# 12. append() Method
# 13. insert() Method
# 14. remove() Method

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. Create an Object
# ===============================================================

# Create an instance of the Person class
# and assign values to the name and age attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Person("Anju", 22)
print("Name :", obj.name)
print("Age  :", obj.age)

# Output:
# Name : Anju
# Age  : 22


print("\n" + "*" * 60)


# ===============================================================
# Q2. Add introduce() Method
# ===============================================================

# Add an introduce() method to the Person class
# that prints a greeting using the name attribute.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

obj = Person("Anju", 22)
obj.introduce()

# Output:
# Hello! My name is Anju.


print("\n" + "*" * 60)


# ===============================================================
# Q3. Method Overriding
# ===============================================================

# Override the introduce() method in the Student class
# to include the student_id in the greeting.

class Person:
    def introduce(self):
        print("Hello!")

class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"Student ID : {self.student_id}")

obj = Student("Anju", 101)
obj.introduce()

# Output:
# Hello! My name is Anju.
# Student ID : 101


print("\n" + "*" * 60)


# ===============================================================
# Q4. Static Method
# ===============================================================

# Create a static method to validate the Student ID.

class Student:

    @staticmethod
    def validate_student_id(student_id):
        if len(str(student_id)) == 5:
            print("Valid Student ID")
        else:
            print("Invalid Student ID")

Student.validate_student_id(12345)

# Output:
# Valid Student ID

# ==================================================================================================================
# Q1 - List Basics

# IMP:
# -> List is an ordered, mutable and heterogeneous data type.
# -> List allows duplicate values.
# -> Indexing starts from 0.
# -> Negative indexing starts from -1.

mylist = ["prashant", "Ashish", "Komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]

print(mylist)
print(type(mylist))

# Indexing
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])

# Slicing
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])   # start : stop : step
print(mylist[:])
print(mylist[::-1])    # Reverse List


# ==================================================================================================================
# Q2 - Update List Element

# IMP:
# List is Mutable means we can modify, update or change its elements.

mylist = ["prashant", "Ashish", "Komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]

print(mylist)

mylist[2] = "Akshay"      # Updating value
print(mylist)


# ==================================================================================================================
# Q3 - Check Element in List

# IMP:
# 'in' operator is used to check whether an element exists in the list.

if "ankush" in mylist:
    print("Yes ankush is available")
else:
    print("Not available")


# ==================================================================================================================
# Q4 - append()

# IMP:
# append() adds a single element at the end of the list.

mylist.append("harsh")
mylist.append("laxman")

print(mylist)


# ==================================================================================================================
# Q5 - insert()

# IMP:
# insert(index, value) inserts an element at the specified index.

mylist.insert(1, "sanket")

print(mylist)


# ==================================================================================================================
# Q6 - remove()

# IMP:
# remove(value) removes the first occurrence of the specified value.

mylist.remove("sandip")

print(mylist)


# ==================================================================================================================
# Q7 - copy()

# IMP:
# copy() creates a duplicate (clone) of the list.

newlist = mylist.copy()

print(newlist)


# ==================================================================================================================
# Q8 - Multidimensional List

# IMP:
# A list inside another list is called a Multidimensional (Nested) List.
# Syntax: list[row][column]

mylist = [
    ["Anju", "Sharma"],
    [85.56],
    [440022, "yyy"]
]

print("Example of Multidimensional List")
print(mylist)

# Accessing elements
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

# Structure
# [
#   ["Anju", "Sharma"],
#   [85.56],
#   [440022, "yyy"]
# ]


# ==================================================================================================================
# Q9 - List Multiplication

# IMP:
# '*' operator repeats the list multiple times.

list1 = ["Anju", "Sharma"]

print(list1 * 2)


# ==================================================================================================================
# Q10 - List Concatenation

# IMP:
# '+' operator joins two lists into one new list.

list2 = [50, 25, 50]

print(list1 + list2)

# ==================================================================================================================
# Q11 - del Keyword

# IMP:
# del is used to delete a particular element or the entire list.
# After deleting the entire list, it cannot be accessed.

list2 = [50, 25, 50, "Anju"]

# del list2[2]      # Delete element at index 2
del list2           # Delete entire list

print(list2)        # NameError: list2 is not defined


# ==================================================================================================================
# Q12 - clear()

# IMP:
# clear() removes all elements from the list.
# The list object still exists, but it becomes empty.

list2 = [50, 25, 50, "Anju"]

list2.clear()

print(list2)


# ==================================================================================================================
# Q13 - Type Casting (String to List)

# IMP:
# list() constructor converts a string into a list of characters.

name = "Anju"

print(name)

myname = list(name)

print(myname)


# ==================================================================================================================
# Q14 - reverse()

# IMP:
# reverse() reverses the order of elements in the same list.
# It modifies the original list.

mylist = [50, 25, 45, 65]

mylist.reverse()

print(mylist)


# ==================================================================================================================
# Q15 - sort() (Ascending Order)

# IMP:
# sort() arranges elements in ascending order by default.
# It modifies the original list.

mylist = [44, 22, 45, 6, 88]

mylist.sort()

print(mylist)


# ==================================================================================================================
# Q16 - sort(reverse=True) (Descending Order)

# IMP:
# reverse=True sorts the list in descending order.

mylist.sort(reverse=True)

print(mylist)

# Note:
# -> Default sorting order for numbers is Ascending.
# -> Default sorting order for strings is Alphabetical.
# -> List should contain homogeneous data (same data type).
# -> Sorting mixed data types (int + str) gives TypeError in Python 3.


# ==================================================================================================================
# Q17 - Aliasing

# IMP:
# Aliasing means two variables refer to the same list object.
# Any changes made through one variable will also reflect in the other.

mylist = [44, 22, 44, 55, 66]

newlist = mylist

print(id(mylist))
print(id(newlist))

mylist[0] = "Anju"

print(mylist)
print(newlist)

# ==================================================================================================================
# Q18 - Membership Operator (in / not in)

# IMP:
# -> Membership Operators are used to check whether an element exists or not.
# -> There are two Membership Operators:
#    1. in
#    2. not in
# -> It returns True or False.

name = "help4code"

print("h" in name)
print("h" not in name)

# Output:
# True
# False


# ==================================================================================================================
# Q19 - for Loop with range()

# IMP:
# -> range() is used to generate a sequence of numbers.
# -> Syntax:
#    range(start, stop, step)
# -> start : Starting value
# -> stop  : Ending value (not included)
# -> step  : Increment / Decrement value

for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# ==================================================================================================================
# Q20 - Reverse Numbers using range()

# IMP:
# -> Negative step (-1) is used to print numbers in reverse order.
# -> Syntax:
#    range(start, stop, -1)

for i in range(10, 0, -1):
    print(i)

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


# ==================================================================================================================
# Q21 - Print Table of 2

# IMP:
# -> Loop runs from 1 to 10.
# -> Each number is multiplied by 2.

for i in range(1, 11):
    print(i * 2)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# ==================================================================================================================
# Q22 - Print Tables from 1 to 20 (Vertical Format)

# IMP:
# -> First loop prints tables from 1 to 10.
# -> Second loop prints tables from 11 to 20.
# -> Each row contains multiplication values.

for i in range(1, 11):
    print(i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10)

print("==================================================")

for j in range(1, 11):
    print(j*11, j*12, j*13, j*14, j*15, j*16, j*17, j*18, j*19, j*20)

# Output:
# 1   2   3   4   5   6   7   8   9   10
# 2   4   6   8   10   12   14   16   18   20
# ...
# 110   120   130   140   150   160   170   180   190   200


# ==================================================================================================================
# Q23 - Traverse List using for Loop

# IMP:
# -> for loop is used to access each element of the list one by one.
# -> No indexing is required.

list3 = [10, 20, 30, 40, 50]

for i in list3:
    print(i)

# Output:
# 10
# 20
# 30
# 40
# 50


# ==================================================================================================================
# Q24 - Sum of List Elements

# IMP:
# -> Initialize sum with 0.
# -> Traverse the list using for loop.
# -> Add each element into sum.
# -> Finally print the total sum.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0

for x in list1:
    sum = sum + x

print("The Sum =", sum)

# Output:
# The Sum = 55

# ==================================================================================================================
# Q25 - continue Statement

# IMP:
# -> continue skips the current iteration.
# -> The loop does not stop.
# -> Control moves to the next iteration.

mycart = [10, 20, 200, 300, 800, 60, 700]

for i in mycart:
    if i > 400:
        print("This is my purchased cart item")
        continue
    print(i)

# Output:
# 10
# 20
# 200
# 300
# This is my purchased cart item
# 60
# This is my purchased cart item


# ==================================================================================================================
# Q26 - break Statement

# IMP:
# -> break terminates the loop immediately.
# -> Remaining iterations are not executed.

mycart = [10, 20, 200, 300, 800, 60, 700]

for i in mycart:
    if i > 400:
        print("This is my purchased cart item")
        break
    print(i)

# Output:
# 10
# 20
# 200
# 300
# This is my purchased cart item


# ==================================================================================================================
# Q27 - Count Odd Numbers

# IMP:
# -> Count variable is used to count odd numbers.
# -> Even numbers satisfy i % 2 == 0.
# -> Odd numbers increase the count.

count = 0

for i in range(9):
    if i % 2 == 0:
        print(i)
    else:
        print(i)
        count += 1

print("Count =", count)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Count = 4


# ==================================================================================================================
# Q28 - Find First Even Number using break

# IMP:
# -> Check whether a number is even.
# -> Stop the loop after finding the first even number.

rollno = [3, 5, 7, 1, 11, 4, 5, 2]

for x in rollno:
    if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
        print("Even no is found", x)
        break

# Output:
# Even no is found 4


# ==================================================================================================================
# Q29 - Weekend or Working Day

# IMP:
# -> Accept a day from the user.
# -> Saturday and Sunday are Weekend.
# -> Remaining days are Working Days.

day = input("Enter Day: ")

if day == "Saturday" or day == "Sunday" or day == "SATURDAY" or day == "SUNDAY":
    print("Weekend")
else:
    print("Working Day")

# Output:
# Enter Day: Sunday
# Weekend


# ==================================================================================================================
# Q30 - Reverse a 3-Digit Number

# IMP:
# -> % (Modulus) gives the last digit.
# -> // (Floor Division) removes the last digit.

num = 123

a = num % 10
num = num // 10

b = num % 10
c = num // 10

rev = a * 100 + b * 10 + c

print("Reverse =", rev)

# Output:
# Reverse = 321


# ==================================================================================================================
# Q31 - Reverse a 7-Digit Number

# IMP:
# -> Extract each digit using % and //.
# -> Multiply each digit according to its place value.

num = 1234567

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10
num = num // 10

e = num % 10
num = num // 10

f = num % 10
g = num // 10

rev = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g

print("Reverse =", rev)

# Output:
# Reverse = 7654321


# ==================================================================================================================
# Q32 - Change Calculation

# IMP:
# -> // is used to calculate the number of notes.
# -> % is used to calculate the remaining amount.

amount = int(input("Please Enter Amount for Withdraw: "))

print("100 Notes =", amount // 100)
print("50 Notes  =", (amount % 100) // 50)
print("20 Notes  =", ((amount % 100) % 50) // 20)
print("10 Notes  =", (((amount % 100) % 50) % 20) // 10)
print("5 Notes   =", ((((amount % 100) % 50) % 20) % 10) // 5)
print("2 Notes   =", (((((amount % 100) % 50) % 20) % 10) % 5) // 2)
print("1 Notes   =", ((((((amount % 100) % 50) % 20) % 10) % 5) % 2) // 1)

# Output:
# Enter Amount: 287
# 100 Notes = 2
# 50 Notes  = 1
# 20 Notes  = 1
# 10 Notes  = 1
# 5 Notes   = 1
# 2 Notes   = 1
# 1 Notes   = 0

# ==================================================================================================================
# Q33 - Nested if...else

# IMP:
# -> Nested if means an if statement inside another if or else.
# -> It is used when multiple conditions need to be checked.

# Syntax:

# if condition:
#     if condition:
#         pass
#     else:
#         pass
# else:
#     if condition:
#         pass
#     else:
#         pass


# ==================================================================================================================
# Q34 - Find Maximum Age

# IMP:
# -> Accept three ages from the user.
# -> Compare them using nested if...else.
# -> Print the greatest age.

age1 = int(input("Enter Age1: "))
age2 = int(input("Enter Age2: "))
age3 = int(input("Enter Age3: "))

if age1 > age2:
    if age1 > age3:
        print("Age1 is Greater =", age1)
    else:
        print("Age3 is Greater =", age3)
else:
    if age2 > age3:
        print("Age2 is Greater =", age2)
    else:
        print("Age3 is Greater =", age3)


# ==================================================================================================================
# Q35 - Check Character Type

# IMP:
# -> Check whether the entered character is:
#    1. Uppercase
#    2. Lowercase
#    3. Digit
#    4. Special Symbol

ch = input("Enter Any Character: ")

if ch.isupper():
    print("Character is Uppercase")
elif ch.islower():
    print("Character is Lowercase")
elif ch.isdigit():
    print("Character is Digit")
else:
    print("Character is Special Symbol")


# ==================================================================================================================
# Q36 - Check Character using ASCII Value

# IMP:
# -> ord() converts a character into its ASCII value.
# -> ASCII Range:
#    A-Z = 65 to 90
#    a-z = 97 to 122
#    0-9 = 48 to 57

ch = ord(input("Enter Any Character: "))

if ch >= 65 and ch <= 90:
    print("Uppercase Character")
elif ch >= 97 and ch <= 122:
    print("Lowercase Character")
elif ch >= 48 and ch <= 57:
    print("Digit")
else:
    print("Special Symbol")


# ==================================================================================================================
# Q37 - Login Validation

# IMP:
# -> Compare username and password.
# -> If both are same, login is successful.

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == password:
    print("Login Successful")
else:
    print("Invalid Login")


# ==================================================================================================================
# Q38 - Login using while Loop

# IMP:
# -> Repeat until correct username and password are entered.
# -> break terminates the loop.

while True:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == password:
        print("Login Successful")
        break
    else:
        print("Invalid Login")


# ==================================================================================================================
# Q39 - find() Method

# IMP:
# -> find() returns the starting index of a substring.
# -> If substring is not found, it returns -1.

s = "help4code is a best platform for practicing programming"

print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))

# Output:
# 0
# -1
# 43


# ==================================================================================================================
# Q40 - join() Method

# IMP:
# -> join() joins multiple strings into one string.
# -> A separator is placed between the strings.

s = ("Anju", "Akshay", "Sharma")

print("  ".join(s))
print(" | ".join(s))

# Output:
# Anju  Akshay  Sharma
# Anju | Akshay | Sharma


# ==================================================================================================================
# Q41 - String Case Methods

# IMP:
# -> lower()
# -> upper()
# -> swapcase()
# -> title()
# -> capitalize()

s = "Python is a High level programming Language"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())


# ==================================================================================================================
# Q42 - format() Method

# IMP:
# -> format() inserts values into a string.

phy = 50
chem = 65
math = 70

print("Physics={} Chemistry={} Math={}".format(phy, chem, math))
print("Physics={0} Chemistry={1} Math={2}".format(phy, chem, math))
print("Physics={x} Chemistry={y} Math={z}".format(x=phy, y=chem, z=math))

total = phy + chem + math

print("Total Marks =", total)
print("Roll No =", "7".zfill(4))


# ==================================================================================================================
# Q43 - Print Characters of String

# IMP:
# -> for loop prints each character one by one.

name = "help4code"

for i in name:
    print(i)


# ==================================================================================================================
# Q44 - Find Character Index

# IMP:
# -> Traverse the string.
# -> Print the index where the required character is found.

name = "prashant"

i = 0

for x in name:
    if x == 'n':
        print("Character found at Index =", i)
        break
    i += 1


# ==================================================================================================================
# Q45 - Print Specific Character

# IMP:
# -> Print only the required character.

a = "shiwaleew"

for i in a:
    if i == 'w':
        print(i)

# Output:
# w
# w


# ==================================================================================================================
# Q46 - Compare Lists

# IMP:
# -> == checks whether values are equal.
# -> != checks whether values are different.

x = ['A', 'B', 'C']
y = ['A', 'B', 'C']
z = [1, 2, 3, 4]

print(x == y)
print(x != y)
print(x != z)

# Output:
# True
# False
# True


# ==================================================================================================================
# Q47 - Arithmetic Expressions

# IMP:
# -> Evaluate expressions using arithmetic operators.

a = 50
b = 30
c = 20
d = 10

print((a + b) * (c / d))
print((a - b) * (c / d))
print(a + (b * c) / d)


# ==================================================================================================================
# Q48 - strip(), lstrip(), rstrip()

# IMP:
# -> strip() removes spaces from both sides.
# -> lstrip() removes spaces from the left.
# -> rstrip() removes spaces from the right.

city = input("Enter Your City: ")

scity = city.strip()

if scity == "Hyderabad":
    print("Hello Hyderabadi... Adab")
elif scity == "Chennai":
    print("Hello Madrasi... Vanakkam")
elif scity == "Bangalore":
    print("Hello Kannadiga... Shubhodya")
else:
    print("Invalid City")


# ==================================================================================================================
# Q49 - replace() Method

# IMP:
# -> replace(old, new) replaces all occurrences of old string with new string.

s = "Python is difficult"

print(s.replace("difficult", "easy"))

s = "abababababab"

print(s.replace("a", "b"))

# Output:
# Python is easy
# bbbbbbbbbbbb

# ==================================================================================================================
# Q50 - Count Special Characters

# IMP:
# -> Traverse the string.
# -> Count only special characters.
# -> Ignore alphabets and digits.

s = "gasgg54@#vscsd!$"

count = 0

for i in s:
    if not i.isalnum():
        count += 1

print("Total Special Characters =", count)

# Output:
# Total Special Characters = 4