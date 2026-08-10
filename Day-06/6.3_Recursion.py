# ===============================================================
# Day 06 – Python Recursion Practice
# ===============================================================

# Topics:
# 1. Recursion
# 2. Factorial using Recursion
# 3. Palindrome using Recursion
# 4. Power using Recursion
# 5. Product of Array using Recursion
# 6. Sum of Numbers using Recursion
# 7. Fibonacci using Recursion
# 8. Mini Exam System using Class and Methods

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. Factorial using Recursion
# ===============================================================

# Recursion:
# When the main problem can be divided into similar subproblems,
# we can use recursion.

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(5))


# ===============================================================
# Q2. Check Palindrome using Recursion
# ===============================================================

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome('awesome'))
# print(isPalindrome('foobar'))
# print(isPalindrome('tacocat'))


# ===============================================================
# Q3. Power using Recursion
# ===============================================================

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0))


# ===============================================================
# Q4. Product of Array using Recursion
# ===============================================================

# def productofArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productofArray(arr[1:])

# print(productofArray([1,2,3]))
# print(productofArray([1,2,3,19]))


# ===============================================================
# Q5. Sum of Numbers using Recursion
# ===============================================================

# def recursiveange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveange(num-1)

# print(recursiveange(6))


# ===============================================================
# Q6. Fibonacci using Recursion
# ===============================================================

# def fib(num):
#     if(num < 2):
#         return num
#     return fib(num - 1) + fib(num-2)

# print(fib(4))


# ===============================================================
# Q7. Mini Exam System using Class and Methods
# ===============================================================

import sys

class Questions:

    def __init__(self):
        self.question = []
        self.option_1 = []
        self.option_2 = []
        self.option_3 = []
        self.option_4 = []
        self.correct_answer = []
        self.countRightAns = 0
        self.countWrongAns = 0
        self.scorePerQue = 5
        self.totalScore = 0
        self.fullName = None
        self.studentId = None

    def personalInfo(self):
        self.fullName = input(" Enter your full Name :")
        self.studentId = int(input('Enter your student Id: '))

    def addQuestions(self):
        self.totalQuestion = int(input("Enter Number of Questions You Want To Add :"))

        for i in range(self.totalQuestion):
            self.question.append(input("Enter question :"))
            self.option_1.append(input("Enter option-1 :"))
            self.option_2.append(input("Enter option-2 :"))
            self.option_3.append(input("Enter option-3 :"))
            self.option_4.append(input("Enter option-4 :"))
            self.correct_answer.append(input("Enter correct answer :"))

    def startExam(self):
        for i in range(self.totalQuestion):

            print("----------------------------------------------------------------------")
            print('Question :', self.question[i])
            print()
            print('Option-1: ', self.option_1[i])
            print('option-2: ', self.option_2[i])
            print('Option-3: ', self.option_3[i])
            print('Option-4: ', self.option_4[i])
            print()
            print('----------------------------------------------------------------------')
            print()

            self.ch = int(input('Enter any one option either 1 or 2 or 3 or 4 :'))

            if self.ch == 1:
                if self.option_1[i] == self.correct_answer[i]:
                    self.totalMarks()
                else:
                    self.countWrongAns += 1

            elif self.ch == 2:
                if self.option_2[i] == self.correct_answer[i]:
                    self.totalMarks()
                else:
                    self.countWrongAns += 1

            elif self.ch == 3:
                if self.option_3[i] == self.correct_answer[i]:
                    self.totalMarks()
                else:
                    self.countWrongAns += 1

            elif self.ch == 4:
                if self.option_4[i] == self.correct_answer[i]:
                    self.totalMarks()
                else:
                    self.countWrongAns += 1

            else:
                print('Invalid choice:')

    def totalMarks(self):
        self.countRightAns += 1
        self.totalScore += self.scorePerQue

    def displayResult(self):
        print("------------------------------------------------------------------")
        print()
        print('Student ID       :', self.studentId)
        print('Student FullName :', self.fullName)
        print('Total Exam Score :', self.totalScore)
        print('Correct Answer   :', self.countRightAns, '  ', 'Wrong Answers :', self.countWrongAns)
        print()
        print('------------------------------------------------------------------')


obj = Questions()  # object creation

while True:

    print('1. Add Student Info:')
    print('2. Admin Add Questions :')
    print('3. Give Exam:')
    print('4. Display Result :')
    print('5. Exit')

    ch = int(input("Enter Your Choice :"))

    if ch == 1:
        obj.personalInfo()

    if ch == 2:
        obj.addQuestions()

    if ch == 3:
        obj.startExam()

    if ch == 4:
        obj.displayResult()

    if ch == 5:
        sys.exit()

# ===============================================================
# End of Day 06 – Recursion Practice
# ===============================================================
