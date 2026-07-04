# ===============================================================
# Day 03 – Python Exception Handling
# ===============================================================

# Topics:
# 1. Basic Exception Handling
# 2. Multiple Exception Handling
# 3. Exception as Message
# 4. Multiple Exceptions in One Except
# 5. Default Except Block
# 6. Else Block
# 7. Finally Block
# 8. Nested Try-Except
# 9. Try-Except-Else-Finally
# 10. User Defined Exception (raise)
# 11. Logging in Python
# 12. Logging with Exception
# 13. Student Result Program
# 14. Menu Driven Calculator
# 15. Product of Array Except Self (Logic)
# 16. Stack Implementation (Menu Driven)
# 17. String Built-in Methods
# ===============================================================


# ===============================================================
# Q1. Basic Exception Handling
# ===============================================================

# except block handles any exception.

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))

try:
    print(a / b)

except:
    print("Can't divide by zero!")

print("Continue")

# Output:
# Enter value of A: 10
# Enter value of B: 0
# Can't divide by zero!
# Continue


print("\n" + "*" * 60)


# ===============================================================
# Q2. Multiple Exception Handling
# ===============================================================

# Different exceptions are handled using separate except blocks.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except ZeroDivisionError:
    print("Can't divide by zero!")

except ValueError:
    print("Enter only integer value.")

print("Continue")

# Output:
# Enter value of A: 10
# Enter value of B: 0
# Can't divide by zero!


print("\n" + "*" * 60)


# ===============================================================
# Q3. Exception as Message
# ===============================================================

# "as message" stores the actual error message.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except ZeroDivisionError as message:
    print("Please ensure you don't divide any number by zero!", message)

except ValueError as message:
    print("Enter only integer value:", message)

# Output:
# Please ensure you don't divide any number by zero!
# division by zero


print("\n" + "*" * 60)


# ===============================================================
# Q4. Multiple Exceptions in One Except
# ===============================================================

# Multiple exceptions can be handled in one except block.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print("Error:", message)

# Output:
# Error: division by zero


print("\n" + "*" * 60)


# ===============================================================
# Q5. Default Except Block
# ===============================================================

# Important:
# Default except block should always be written last.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number:", message)

except:
    print("This is the default except block.")

# Output:
# Enter correct number: division by zero


print("\n" + "*" * 60)


# ===============================================================
# Q6. Else Block
# ===============================================================

# else executes only if no exception occurs.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print("Error:", message)

else:
    print("Everything is OK!")

# Output:
# 5.0
# Everything is OK!


print("\n" + "*" * 60)


# ===============================================================
# Q7. Finally Block
# ===============================================================

# finally block always executes.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print("Error:", message)

finally:
    print("I will always execute!")

# Output:
# Error: division by zero
# I will always execute!


print("\n" + "*" * 60)


# ===============================================================
# Q8. Nested Try-Except
# ===============================================================

# A try block can be placed inside another try block.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))

    try:
        print(a / b)

    except ZeroDivisionError as message:
        print("Can't divide by zero:", message)

except ValueError as message:
    print("Enter correct number:", message)

# Output:
# Can't divide by zero: division by zero

print("\n" + "*" * 60)

# ===============================================================
# Q9. Try - Except - Else - Finally
# ===============================================================

# else executes if no exception occurs.
# finally always executes.

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print(message)

else:
    print("There are no errors in try block.")

finally:
    print("I am finally block. I always execute.")

# Output:
# Enter value of A: 10
# Enter value of B: 2
# 5.0
# There are no errors in try block.
# I am finally block. I always execute.


print("\n" + "*" * 60)

# ===============================================================
# Q10. User Defined Exception (raise)
# ===============================================================

# raise keyword is used to generate an exception manually.

bank_bal = 500

if bank_bal < 2000:
    raise Exception("Your account balance is below the minimum limit.")

else:
    print("Your amount has been withdrawn!")

# Output:
# Exception: Your account balance is below the minimum limit.


print("\n" + "*" * 60)

# ===============================================================
# Q11. Logging in Python
# ===============================================================

# Logging stores program information in a file.

import logging

logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

logging.debug("This indicates debugging information.")
logging.info("This indicates important information.")
logging.error("This indicates error information.")
logging.warning("This indicates warning information.")
logging.critical("This indicates critical information.")

print("Logs are saved in newfile.txt")

# Output:
# Logs are saved in newfile.txt


print("\n" + "*" * 60)

# ===============================================================
# Q12. Logging with Exception
# ===============================================================

# exception() stores the error details in the log file.

import logging

logging.basicConfig(filename="arithmatic.txt", level=logging.DEBUG)

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as message:
    print(message)
    logging.exception(message)

print("Logging level is set up. Check 'arithmatic.txt'.")

# Output:
# division by zero
# Logging level is set up. Check 'arithmatic.txt'.


print("\n" + "*" * 60)

# ===============================================================
# Q13. Student Result Program
# ===============================================================

phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chemistry Marks: "))
math = int(input("Enter Maths Marks: "))

total = phy + chem + math
percentage = total / 3

print("Total Marks =", total)
print("Percentage =", percentage)

if phy >= 40 and chem >= 40 and math >= 40:
    print("Result : PASS")
else:
    print("Result : FAIL")

gender = input("Enter Gender (M/F): ")

if percentage >= 65 and gender.upper() == "M":
    print("Eligible for Placement")

else:
    print("Not Eligible for Placement")

# Output:
# Total Marks = ...
# Percentage = ...
# PASS / FAIL
# Eligible / Not Eligible


print("\n" + "*" * 60)

# ===============================================================
# Q14. Menu Driven Calculator
# ===============================================================

# Menu Driven Program using Functions.

import sys

def add():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Addition =", a + b)

def sub():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Subtraction =", a - b)

def div():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Division =", a / b)

def mul():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Multiplication =", a * b)

while True:

    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        sub()

    elif choice == 3:
        div()

    elif choice == 4:
        mul()

    elif choice == 5:
        sys.exit()

    else:
        print("Invalid Choice!")



print("\n" + "*" * 60)

# ===============================================================
# Q15. Product of Array Except Self
# ===============================================================

# Problem:
# Return an array where each element is the product
# of all other elements except itself.

# Example:
# Input  : [1, 2, 3, 4]
# Output : [24, 12, 8, 6]

# Logic:
# Use Prefix Product + Suffix Product.


print("\n" + "*" * 60)

# ===============================================================
# Q16. Stack Implementation (Menu Driven)
# ===============================================================

# Stack Operations:
# Push
# Pop
# Peek
# Display
# Delete

# (Use your Stack class program here.)



print("\n" + "*" * 60)

# ===============================================================
# Q17. String Built-in Methods
# ===============================================================

print("isalnum():", "Anjusharma777".isalnum())

print("isalpha():", "Anjusharma777".isalpha())

print("isdigit():", "777f".isdigit())

print("islower():", "sdsdsd".islower())

print("Empty islower():", "".islower())

print("isupper():", "ANJUSHARMA".isupper())

print("istitle():", "My Name Is Anju".istitle())

print("Empty istitle():", "".istitle())

print("isspace():", "".isspace())

print("startswith():", "Hello".startswith("He"))

print("endswith():", "hello".endswith("lo"))

# Output:
# isalnum(): True
# isalpha(): False
# isdigit(): False
# islower(): True
# Empty islower(): False
# isupper(): True
# istitle(): True
# Empty istitle(): False
# isspace(): False
# startswith(): True
# endswith(): True