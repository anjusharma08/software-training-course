# ===============================================================
# Day 05 – Python Dictionary Practice
# ===============================================================

# Topics:
# 1. Dictionary Creation
# 2. Access Value using Key
# 3. Update Dictionary Value
# 4. Print Dictionary Keys
# 5. Print Dictionary Values
# 6. Print Key-Value Pairs
# 7. Add New Key-Value Pair
# 8. pop() Method
# 9. copy() Method
# 10. Check Empty Dictionary
# 11. Find Maximum Value and Key
# 12. Reverse Key-Value Pairs
# 13. keys() Method
# 14. get() Method
# 15. Membership Operator
# 16. len() Function
# 17. popitem() Method
# 18. clear() Method
# 19. Merge Two Dictionaries
# 20. Sum of Dictionary Values
# 21. Find Minimum Value and Key
# 22. Count Dictionary Items

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. Create a Dictionary
# ===============================================================

mydic = {
    101: "prashant",
    102: "ashish",
    "103": "monini",
    "104": "trivani",
    101: "ashish",
    104: "ashish",
}

print(mydic)
print(type(mydic))

# With the help of key print values
a = mydic[102]
print(a)


# ===============================================================
# Q2. Update Dictionary Value
# ===============================================================

# Replace old value with new value

mydic[102] = "peter"

print(mydic)


# ===============================================================
# Q3. Print Dictionary Keys
# ===============================================================

for x in mydic:
    print(x)


# ===============================================================
# Q4. Print Dictionary Values
# ===============================================================

for x in mydic.values():
    print(x)


# ===============================================================
# Q5. Print Key-Value Pairs
# ===============================================================

for x, y in mydic.items():
    print(x, y)


# ===============================================================
# Q6. Add New Key-Value Pair
# ===============================================================

mydic["mobile_no"] = 12455545

print(mydic)


# ===============================================================
# Q7. pop() Method
# ===============================================================

mydic = {
    101: "prashant",
    "professional": "developer",
    "empid": 1010
}

mydic.pop(101)

print(mydic)

# pop() method removes pair by specific key name


# ===============================================================
# Q8. copy() Method
# ===============================================================

mydic = {
    101: "prashant",
    "professional": "developer",
    "empid": 1010
}

newdic = mydic.copy()

print(newdic)


# ===============================================================
# Q9. Check Empty Dictionary
# ===============================================================

d = {}

def check_dict(d):
    if not d:
        print("Empty")
    else:
        print("Not Empty")

check_dict(d)


# ===============================================================
# Q10. Find Maximum Value and Key
# ===============================================================

mydict = {"A": 50, "B": 30, "c": 70}

highest_key = max(mydict, key=mydict.get)

print(mydict[highest_key])
print(highest_key)

# With function

d = {"A": 50, "B": 30, "c": 70}

def max_key(d):
    key = max(d, key=d.get)
    print(key)

max_key(d)


# ===============================================================
# Q11. Reverse Key-Value Pairs
# ===============================================================

dic = {
    "A": 1,
    "B": 2,
    "c": 3
}

reverse_dic = {value: key for key, value in dic.items()}

print(reverse_dic)


# ===============================================================
# Q12. keys() Method
# ===============================================================

mydic = {
    "name": "Anju",
    "age": 22,
    "course": "MCA"
}

print(mydic.keys())


# ===============================================================
# Q13. get() Method
# ===============================================================

mydic = {
    "name": "Anju",
    "age": 22,
    "course": "MCA"
}

print(mydic.get("name"))
print(mydic.get("city"))


# ===============================================================
# Q14. Check Key using Membership Operator
# ===============================================================

mydic = {
    "name": "Anju",
    "age": 22,
    "course": "MCA"
}

if "name" in mydic:
    print("Key is available")
else:
    print("Key is not available")


# ===============================================================
# Q15. Find Length of Dictionary
# ===============================================================

mydic = {
    "A": 50,
    "B": 30,
    "C": 70
}

print("Length =", len(mydic))


# ===============================================================
# Q16. popitem() Method
# ===============================================================

mydic = {
    "A": 50,
    "B": 30,
    "C": 70
}

mydic.popitem()

print(mydic)


# ===============================================================
# Q17. clear() Method
# ===============================================================

mydic = {
    "A": 50,
    "B": 30,
    "C": 70
}

mydic.clear()

print(mydic)


# ===============================================================
# Q18. Merge Two Dictionaries
# ===============================================================

dic1 = {
    "A": 10,
    "B": 20
}

dic2 = {
    "C": 30,
    "D": 40
}

dic1.update(dic2)

print(dic1)


# ===============================================================
# Q19. Sum of Dictionary Values
# ===============================================================

mydic = {
    "A": 10,
    "B": 20,
    "C": 30
}

total = sum(mydic.values())

print("Sum =", total)


# ===============================================================
# Q20. Find Minimum Value and Key
# ===============================================================

mydic = {
    "A": 50,
    "B": 30,
    "C": 70
}

lowest_key = min(mydic, key=mydic.get)

print(mydic[lowest_key])
print(lowest_key)


# ===============================================================
# Q21. Count Dictionary Items
# ===============================================================

mydic = {
    "A": 50,
    "B": 30,
    "C": 70,
    "D": 90
}

count = len(mydic)

print("Total Items =", count)
