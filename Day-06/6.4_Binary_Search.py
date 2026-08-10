# ===============================================================
# Day 06 – Python Binary Search Practice
# ===============================================================

# Topics:
# 1. Binary Search
# 2. Student Marks Dictionary
# 3. Bubble Sort

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. Binary Search
# ===============================================================

# def binarySearch(array, target):
#     low = 0
#     high = len(array)-1
#
#     while low <= high:
#         mid = (low+high)//2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#
#     return -1
#
# array = [1,2,3,4,5,6,7,8,9]
# target = 7
#
# result = binarySearch(array, target)
#
# if result != -1:
#     print("Element found at index no ", result)
# else:
#     print("Element not found")


# ===============================================================
# Q2. Student Name and Marks Dictionary
# ===============================================================

# Write a program to take student name and marks from the
# keyword and create a dictionary. Also display student marks
# by taking student name as input.

# n = int(input("Enter the number of student:- "))
# d = {}
#
# for i in range(n):
#     name = input("Enter the student name:- ")
#     marks = int(input("Enter the marks:-   "))
#     d[name] = marks
#
# while True:
#     name = input("Enter Student name to get marks: ")
#     marks = d.get(name, -1)
#
#     if marks == -1:
#         print("Student not found")
#     else:
#         print("The marks of ", name, "are", marks)
#
#     option = input("Do you want to find another student marks[yes/no]")
#
#     if option == "No":
#         break
#
# print("Thanks for using our application")


# ===============================================================
# Q3. Bubble Sort
# ===============================================================

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


array = [64,34,25,12,22,11,90]

bubbleSort(array)

# ===============================================================
# End of Day 06 – Binary Search Practice
# ===============================================================
