# ===============================================================
# Day 06 – Python Functions & Pattern Practice
# ===============================================================

# Topics:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable-Length Arguments
# 5. Returning Multiple Values
# 6. Nested for Loop
# 7. Number Patterns
# 8. Star Patterns
# 9. Alphabet Patterns
# 10. Pattern Printing using chr()
# 11. time.sleep() with Patterns

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. Positional Argument
# ===============================================================

# def msg(val1,val2):
#     print("Value1 = ",val1)
#     print("Value2 = ",val2)

# # calling function
# msg("admin","help4code")


# ===============================================================
# Q2. Keyword Argument
# ===============================================================

# def msg(val1,val2):
#     print("Value1 = ",val1)
#     print("Value2 = ",val2)

# # calling function
# msg(val1="admin",val2="help4code")


# ===============================================================
# Q3. Default Argument
# ===============================================================

# def city(cityname="Nagpur"):
#     print("City name : ",cityname)

# city("Mumbai")
# city("Nashik")
# city()


# ===============================================================
# Q4. Variable Length Argument / Variable Number of Argument
# ===============================================================

# def cityname(*city):  # .....accept everything by *
#     print(city)

# cityname("Nagpur","Nashik","Pune","Delhi","Indore")


# ===============================================================
# Q5. Function Return Multiple Values at Same Time in Python
# ===============================================================

# def arithmatic(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div  # .........return multiple value same time

# print(arithmatic(5,5))


# ===============================================================
# Q6. Nested for Loop
# ===============================================================

# for i in range(1,4):  # outer loop ==> row
#     for j in range(1,4):  # inner loop ==> col
#         print(i,end=" ")
#     print()

# Output:
# 1 1 1
# 2 2 2
# 3 3 3


# ===============================================================
# Q7. Number Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# Output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5


# ===============================================================
# Q8. Reverse Number Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

# Output:
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1


# ===============================================================
# Q9. Star Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))

# for i in range(1,n+1):
#     print("*"*i)

# Output:
# *
# **
# ***
# ****
# *****


# ===============================================================
# Q10. Alphabet Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))

# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=(" "))
#     print()

# Output:
# A
# B B
# C C C
# D D D D
# E E E E E


# ===============================================================
# Q11. Reverse Star Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))

# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *


# ===============================================================
# Q12. Reverse Alphabet Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- "))  # 5

# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=(" "))
#     print()

# Output:
# A A A A A
# B B B B
# C C C
# D D
# E


# ===============================================================
# Q13. Number Pattern with time.sleep()
# ===============================================================

# import time

# n=int(input("Enter the number of rows:- ")) # 5

# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i,end=(" "))
#     print()

# Output:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1


# ===============================================================
# Q14. Reverse Alphabet Pattern
# ===============================================================

# n=int(input("Enter the number of rows:- ")) # 5

# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=(" "))
#     print()

# Output:
# E E E E E
# D D D D
# C C C
# B B
# A


# ===============================================================
# Q15. Star Pattern with time.sleep()
# ===============================================================

# import time

# n=int(input("Enter the number of rows:- ")) # 5

# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# ===============================================================
# End of Day 06 – Functions & Pattern Practice
# ===============================================================
