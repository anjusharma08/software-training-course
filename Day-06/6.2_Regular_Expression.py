# ===============================================================
# Day 06 – Python Regular Expression Practice
# ===============================================================

# Topics:
# 1. Regular Expression
# 2. re.compile()
# 3. finditer()
# 4. match()
# 5. fullmatch()
# 6. search()
# 7. findall()
# 8. sub()
# 9. subn()
# 10. E-Mail Validation
# 11. Mobile Number Validation
# 12. Search Text from a File

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. finditer() with Regular Expression
# ===============================================================

# import re
# re module for performing all the regular expression based operations

# count = 0
# to count the number of matching found

# pattern = re.compile("The")
# string converts into bytecode

# matcher = pattern.finditer(
#     "The students emerge with original pieces of writing, "
#     "more confident in their skills and connected to a supportive "
#     "writing community. The"
# )

# print(matcher)

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences: ", count)

# Output:
# 0 ... 3 ... The
# 141 ... 144 ... The
# The number of occurrences:  2


# ===============================================================
# Q2. finditer() Function
# ===============================================================

# import re

# count = 0
# matcher = re.finditer("HI","HIHIHIHI")

# print(matcher)

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences: ", count)

# Output:
# 0 ... 2 ... HI
# 2 ... 4 ... HI
# 4 ... 6 ... HI
# 6 ... 8 ... HI
# The number of occurrences: 4


# ===============================================================
# Q3. Search Character using finditer()
# ===============================================================

# import re

# obj = input("Enter any character :- ")

# objmatch = re.finditer(obj, "a7b @k9z")

# count = 0

# for i in objmatch:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences: ", count)


# ===============================================================
# Q4. match() Function
# ===============================================================

# import re

# a = input("Enter string to perform match operation:-  ")

# mtch = re.match(a, "Python is very important language")

# print(mtch)

# if mtch != None:
#     print("Match found at beginning level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("There is no matching at beginning level")

# Output:
# Enter string to perform match operation:- Python
# <re.Match object; span=(0, 6), match='Python'>
# Match found at beginning level
# 0 6


# ===============================================================
# Q5. fullmatch() Function
# ===============================================================

# import re

# a = input("Enter string to perform match operation:-  ")

# mtch = re.fullmatch(a, "pythonisvery")

# print(mtch)

# if mtch != None:
#     print("Match found")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("Full match not found")

# Output:
# Enter string to perform match operation:- pythonisvery
# <re.Match object; span=(0, 12), match='pythonisvery'>
# Match found
# 0 12


# ===============================================================
# Q6. search() Function
# ===============================================================

# import re

# a = input("Enter string to perform match operation:-  ")

# mtch = re.search(a, "python is very")

# print(mtch)

# if mtch != None:
#     print("Match found")
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching anywhere")

# Output:
# Enter string to perform match operation:- very
# <re.Match object; span=(10, 14), match='very'>
# Match found
# 10 14 very


# ===============================================================
# Q7. findall() Function
# ===============================================================

# import re

# mtch = re.findall('[^0-9a-zA-Z]', "abcdef235@#SNDJDBJ")

# print(mtch)

# Match character classes


# ===============================================================
# Q8. sub() Function
# ===============================================================

# import re

# obj = re.sub('[a-z]', 'X', '2345 ABCD Fabc deff')

# print(obj)

# Output:
# 2345 ABCD FXXX XXXX


# ===============================================================
# Q9. subn() Function
# ===============================================================

# import re

# obj = re.subn('[0-7]', '@', 'ab3gd6nk17')

# print(obj)

# print("The student is : ", obj[0])
# print("The number of replacement is : ", obj[1])

# Output:
# ('ab@gd@nk@@', 4)
# The student is : ab@gd@nk@@
# The number of replacement is : 4


# ===============================================================
# Q10. Validate E-Mail ID
# ===============================================================

# import re

# s = input("Enter mail id : ")

# m = re.fullmatch(r"[a-zA-Z0-9_.]+@gmail[.]com", s)

# if m != None:
#     print("Valid E-Mail id")
# else:
#     print("Invalid E-mail id")


# ===============================================================
# Q11. Accept College E-Mail ID
# ===============================================================

# Write a program to accept college e-mail and e-mail.


# ===============================================================
# Q12. Validate Mobile Number
# ===============================================================

# import re

# mo = input("Enter mobile number")

# obj = re.fullmatch("[05]\\d{9}", mo)

# if obj != None:
#     print("Valid mobile number")
# else:
#     print("invalid mobile number")


# ===============================================================
# Q13. Search Text from a File
# ===============================================================

import re

a = input("Enter string to perform match operation: ")

f = open("mymyfile.txt", 'r')
c = f.read()
f.close()

mtch = re.search(a, c)

print(mtch)

if mtch != None:
    print("Match found at beginning level")
    print(mtch.start(), " ", mtch.end())
else:
    print("There is no matching at beginning level")

# ===============================================================
# End of Day 06 – Regular Expression Practice
# ===============================================================
