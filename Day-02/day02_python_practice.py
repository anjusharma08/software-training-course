# ===============================================================
# Day 02 – Python OOPs (Object-Oriented Programming)
# ===============================================================

# Topics:
# 1. Class and Object
# 2. Constructor
# 3. Instance Variables
# 4. Parameterized Constructor
# 5. Static Variables
# 6. Class Method
# 7. Static Method
# 8. Instance Variable Manipulation (Add/Delete)
# 9. Single Inheritance
# 10. Multilevel Inheritance
# 11. Multiple Inheritance
# 12. Abstraction
# 13. Polymorphism
# 14. Method Overriding
# 15. super() Function
# 16. Encapsulation
# 17. Public, Protected and Private Members
# 18. Garbage Collector

# ===============================================================
# Q1. Class, Object and Data Member
# ===============================================================

class Student:
    rollno = 101  # Data Member

    def msg(self):
        print("Hello World")

obj = Student()
print(obj.rollno)
obj.msg()
print(obj)

# Output:
# 101
# Hello World
# <__main__.Student object at 0x...>


print("\n" + "*" * 60)


# ===============================================================
# Q2. Constructor Example
# ===============================================================

class Demo:
    def __init__(self):
        print("I am a Constructor And I am always called first!!")

    def info(self):
        print("One Object")

obj = Demo()
obj.info()

obj2 = Demo()

# Output:
# I am a Constructor And I am always called first!!
# One Object
# I am a Constructor And I am always called first!!


print("\n" + "*" * 60)


# ===============================================================
# Q3. Constructor with Instance Variables
# ===============================================================

class Hod:
    def __init__(self):
        self.name = "Anju Sharma"
        self.age = 22
        self.empid = 101

    def info(self):
        print("My name is :", self.name)
        print("My age is :", self.age)
        print("My emp id is :", self.empid)

obj = Hod()
obj.info()

# Output:
# My name is : Anju Sharma
# My age is : 22
# My emp id is : 101


print("\n" + "*" * 60)


# ===============================================================
# Q4. Parameterized Constructor
# ===============================================================

class Hod:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def show(self):
        print("My name is :", self.name)
        print("My age is :", self.age)
        print("My rollno is :", self.rollno)

obj = Hod("Anju", 22, 101)
obj.show()

# Output:
# My name is : Anju
# My age is : 22
# My rollno is : 101


print("\n" + "*" * 60)


# ===============================================================
# Q5. Instance Variable
# ===============================================================

class New:
    def __init__(self):
        self.a = 10

obj1 = New()
obj2 = New()
obj3 = New()

obj1.a = 20

print(obj1.a)
print(obj2.a)
print(obj3.a)

# Output:
# 20
# 10
# 10


print("\n" + "*" * 60)


# ===============================================================
# Q6. Static Variable
# ===============================================================

class New:
    a = 10

    def __init__(self):
        self.name = "Anju"

obj1 = New()
obj2 = New()
obj3 = New()

New.a = 50

print(obj1.a)

# Output:
# 50


print("\n" + "*" * 60)


# ===============================================================
# Q7. Static Variable vs Instance Variable
# ===============================================================

class College:
    collegename = "Modern College"

    def __init__(self):
        self.studentname = "Prashant"

principal = College()
teacher = College()
accountant = College()

print("Principal =", principal.collegename, "|", principal.studentname)
print("Teacher =", teacher.collegename, "|", teacher.studentname)
print("Accountant =", accountant.collegename, "|", accountant.studentname)

College.collegename = "HBD"
principal.studentname = "Prashant Jha"

print("\nAfter Modification:\n")

print("Principal =", principal.collegename, "|", principal.studentname)
print("Teacher =", teacher.collegename, "|", teacher.studentname)
print("Accountant =", accountant.collegename, "|", accountant.studentname)

# Output:
# Principal = Modern College | Prashant
# Teacher = Modern College | Prashant
# Accountant = Modern College | Prashant
#
# After Modification:
#
# Principal = HBD | Prashant Jha
# Teacher = HBD | Prashant
# Accountant = HBD | Prashant

# ===============================================================
# Q8. Adding and Deleting Instance Variables
# ===============================================================

# Important:
# We can add a new instance variable using an object.
# We can also delete an existing instance variable.

class Student:
    def __init__(self):
        self.s_name = input("Enter your name: ")
        self.s_rollno = 101   # Instance Variable

    def getdata(self):
        self.s_mb = 2525252525   # Instance Variable

obj = Student()
obj.getdata()

obj.s_branch = "CS"      # Adding new instance variable
del obj.s_rollno         # Deleting instance variable

print(obj.__dict__)

# Sample Output:
# Enter your name: Anju
# {'s_name': 'Anju', 's_mb': 2525252525, 's_branch': 'CS'}


print("\n" + "*" * 60)


# ===============================================================
# Q9. Class Method
# ===============================================================

# Important:
# Class methods work with class variables.
# They are created using the @classmethod decorator.

class Student:
    college = "Modern College"

    @classmethod
    def changeCollege(cls, name):
        cls.college = name

Student.changeCollege("ABC College")

print(Student.college)

# Output:
# ABC College


print("\n" + "*" * 60)


# ===============================================================
# Q10. Static Method
# ===============================================================

# Important:
# Static methods do not use self or cls.
# They are created using the @staticmethod decorator.

class Student:

    @staticmethod
    def get_personal_detail(firstname, lastname):
        print("Your personal details:", firstname, lastname)

    @staticmethod
    def contact_detail(mobile_no, rollno):
        print("Your contact details:", mobile_no, rollno)

Student.get_personal_detail("Anju", "Sharma")
Student.contact_detail(9876543210, 101)

# Output:
# Your personal details: Anju Sharma
# Your contact details: 9876543210 101


print("\n" + "*" * 60)


# ===============================================================
# Q11. Single Level Inheritance
# ===============================================================

# Important:
# One child class inherits from one parent class.

class College:

    def college_name(self):
        print("Modern College")


class Student(College):

    def student_info(self):
        print("Name: Anju Sharma")
        print("Branch: Computer Application")


obj = Student()

obj.college_name()
obj.student_info()

# Output:
# Modern College
# Name: Anju Sharma
# Branch: Computer Application


print("\n" + "*" * 60)


# ===============================================================
# Q12. Multilevel Inheritance
# ===============================================================

# Important:
# One class inherits another child class.

class College:

    def college_name(self):
        print("Modern College")


class Student(College):

    def student_info(self):
        print("Name: Anju Sharma")
        print("Branch: Computer Application")


class Exam(Student):

    def subject(self):
        print("Subject1: Design Engineering")
        print("Subject2: Maths")
        print("Subject3: C Language")


obj = Exam()

obj.college_name()
obj.student_info()
obj.subject()

# Output:
# Modern College
# Name: Anju Sharma
# Branch: Computer Application
# Subject1: Design Engineering
# Subject2: Maths
# Subject3: C Language


print("\n" + "*" * 60)


# ===============================================================
# Q13. Multiple Inheritance
# ===============================================================

# Important:
# One child class inherits from multiple parent classes.

class SubMarks:

    math = int(input("Enter Math Marks: "))
    de = int(input("Enter DE Marks: "))
    c = int(input("Enter C Marks: "))
    english = int(input("Enter English Marks: "))


class PractMarks:

    cpract = int(input("Enter Practical Marks: "))


class Result(SubMarks, PractMarks):

    def total(self):
        if self.math >= 40 and self.de >= 40 and self.c >= 10 and self.english >= 40 and self.cpract >= 20:
            print("Pass")
        else:
            print("Fail")


obj = Result()
obj.total()

# Sample Output:
# Enter Math Marks: 80
# Enter DE Marks: 75
# Enter C Marks: 35
# Enter English Marks: 65
# Enter Practical Marks: 25
# Pass


print("\n" + "*" * 60)


# ===============================================================
# Q14. Abstraction
# ===============================================================

# Important:
# Abstract classes cannot create objects directly.
# Child classes must implement all abstract methods.

from abc import ABC, abstractmethod


class Hel4Code(ABC):

    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def placement(self):
        pass


class Ashish(Hel4Code):

    def training(self):
        print("C, C++, Java")

    def placement(self):
        print("Java Placement")


class Ankush(Hel4Code):

    def training(self):
        print("Python Django")

    def placement(self):
        print("Python Placement")


obj = Ashish()
obj.training()
obj.placement()

obj = Ankush()
obj.training()
obj.placement()

# Output:
# C, C++, Java
# Java Placement
# Python Django
# Python Placement


print("\n" + "*" * 60)


# ===============================================================
# Q15. Real-Life Abstraction Example (IRCTC)
# ===============================================================

# Important:
# Different classes provide their own implementation of the same method.

from abc import ABC, abstractmethod


class IRCTC(ABC):

    @abstractmethod
    def bookTicket(self):
        pass


class MakeMyTrip(IRCTC):

    def bookTicket(self):
        print("Welcome to MakeMyTrip")


class GoIbibo(IRCTC):

    def bookTicket(self):
        print("Welcome to GoIbibo")


class Yatra(IRCTC):

    def bookTicket(self):
        print("Welcome to Yatra")


MakeMyTrip().bookTicket()
GoIbibo().bookTicket()
Yatra().bookTicket()

# Output:
# Welcome to MakeMyTrip
# Welcome to GoIbibo
# Welcome to Yatra

# ===============================================================
# Q16. Polymorphism (Method Overloading)
# ===============================================================

# Important:
# Python does NOT support Method Overloading.
# The last method with the same name overrides the previous ones.

class Arithmetic:

    def add(self, a, b, c):
        print("Addition =", a + b + c)


obj = Arithmetic()
obj.add(10, 20, 30)

# Output:
# Addition = 60


print("\n" + "*" * 60)


# ===============================================================
# Q17. Constructor Overloading
# ===============================================================

# Important:
# Python does NOT support Constructor Overloading.
# Only the last constructor is considered.

class Arithmetic:

    def __init__(self, a, b):
        print("Passing Two Arguments")
        print("Values:", a, b)


obj = Arithmetic(10, 20)

# Output:
# Passing Two Arguments
# Values: 10 20


print("\n" + "*" * 60)


# ===============================================================
# Q18. Method Overriding
# ===============================================================

# Important:
# Child class overrides the parent's method.
# super() is used to call the parent class method.

class RBI:

    def homeloan(self):
        print("Home Loan Interest Rate: 8%")

    def carloan(self):
        print("Car Loan Interest Rate: 8%")


class SBI(RBI):

    def homeloan(self):
        print("Home Loan Interest Rate: 10.5%")
        super().homeloan()


sbiObj = SBI()

sbiObj.homeloan()
sbiObj.carloan()

# Output:
# Home Loan Interest Rate: 10.5%
# Home Loan Interest Rate: 8%
# Car Loan Interest Rate: 8%


print("\n" + "*" * 60)


# ===============================================================
# Q19. Using super() in Constructor
# ===============================================================

# Important:
# super() is used to call the parent class constructor.

class Father:

    def __init__(self):
        print("Father: I am on time at breakfast table")


class Child(Father):

    def __init__(self):
        super().__init__()
        print("Child: I will be late for breakfast")


obj = Child()

# Output:
# Father: I am on time at breakfast table
# Child: I will be late for breakfast


print("\n" + "*" * 60)


# ===============================================================
# Q20. Encapsulation (Public, Private and Protected Members)
# ===============================================================

# Important:
# Public   -> Accessible everywhere.
# Protected -> Accessible within class and child class (_variable).
# Private  -> Accessible only inside the same class (__variable).


# ---------------- Public Variable ----------------

class Base:

    def __init__(self):
        self.name = "Anju"     # Public Variable


obj = Base()

print("Public Variable:", obj.name)

# Output:
# Public Variable: Anju


print("\n------------------------------")


# ---------------- Protected Variable ----------------

class Base:

    def __init__(self):
        self._city = "Indore"      # Protected Variable


class Derived(Base):

    def show(self):
        print("Protected Variable:", self._city)


obj = Derived()
obj.show()

# Output:
# Protected Variable: Indore


print("\n------------------------------")


# ---------------- Private Variable ----------------

class Base:

    def __init__(self):
        self.__password = "Python123"     # Private Variable

    def showPassword(self):
        print("Private Variable:", self.__password)


obj = Base()
obj.showPassword()

# Output:
# Private Variable: Python123


print("\n------------------------------")


# ---------------- Public and Private Methods ----------------

class RBI:

    def publicPolicy(self):
        print("Public Policy of RBI")

    def __privatePolicy(self):
        print("Private Policy of RBI")

    def accessPrivateMethod(self):
        self.__privatePolicy()


obj = RBI()

obj.publicPolicy()
obj.accessPrivateMethod()

# Output:
# Public Policy of RBI
# Private Policy of RBI


print("\n" + "*" * 60)


# ===============================================================
# Extra Topic: Garbage Collector
# ===============================================================

# Important:
# Garbage Collector automatically removes unused objects from memory.
# It helps in efficient memory management.

import gc

print("Garbage Collector Enabled:", gc.isenabled())

# Output:
# Garbage Collector Enabled: True