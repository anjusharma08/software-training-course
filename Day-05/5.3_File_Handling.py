# ===============================================================
# Day 05 – Python File Handling Practice
# ===============================================================

# Topics:
# 1. File Handling
# 2. File Properties
# 3. Writing Data into a File
# 4. Override File Data
# 5. Append Data
# 6. writelines()
# 7. Reading Data from a File
# 8. with Statement
# 9. Copy Image using Binary Mode
# 10. CSV File Handling
# 11. Store Student Records
# 12. Student Marks and Percentage

# ===============================================================
# Practice Questions
# ===============================================================


# ===============================================================
# Q1. File Handling
# ===============================================================

# Whenever you want to use/store data in future purpose,
# so we use file handling.

# f = open("myfile.text","w")

# print("Name of file : ",f.name)
# print("file mode : ",f.mode)
# print("readable : ",f.readable())
# print("writeable : ",f.writable())
# print("file closed : ",f.name)

# f.close()

# print("file closed : ",f.closed)


# ===============================================================
# Q2. Write Data into a File
# ===============================================================

# f = open("myfile.text","w")

# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Nashik is a smart city")
# f.write("\n Mumbai is a smart city")

# f.close()

# print("file operation is done")


# ===============================================================
# Q3. Override File Data
# ===============================================================

# f = open("myfile.text","w")

# f.write("\n Pune is a smart city")

# f.close()

# print("file operation is done")


# ===============================================================
# Q4. Append Data
# ===============================================================

# f = open("myfile.text","a")

# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Nashik is a smart city")
# f.write("\n Mumbai is a smart city")
# f.write("\n Indore is a smart city ")

# f.close()

# print("file operation is done")


# ===============================================================
# Q5. Insert List into a File
# ===============================================================

# f = open("myfile.text","w")

# mylist = ["prashant"," ","mahesh"," ","suresh"," "]

# f.writelines(mylist)

# f.close()

# print("written work has done successfully")


# ===============================================================
# Q6. Read Data from a File
# ===============================================================

# f = open("myfile.text","r")

# print((f.read()))

# f.close()


# ===============================================================
# Q7. Properties of File Object
# ===============================================================

# with open("myfile.txt","w") as f:

#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")

#     print("file closed : ",f.closed)
#     print("file closed : ",f.closed)


# ===============================================================
# Q8. Read File using with Statement
# ===============================================================

# with open("myfile.txt","r") as f :

#     content = f.read()

# print(content)


# ===============================================================
# Q9. Copy Image
# ===============================================================

# f1 = open("image.jpeg","rb")
# f2 = open("image1.jpg","wb")

# data = f1.read()

# f2.write(data)


# ===============================================================
# Q10. CSV Model
# ===============================================================

# import csv

# f = open("student.csv","a",newline="")

# a = csv.writer(f) # here it will return csvwriter object

# a.writerow(["studentID","rollno","name","mobileno"])


# ===============================================================
# Q11. Store Student Record in CSV File
# ===============================================================

# import csv

# f = open("student.csv","a",newline="")

# a = csv.writer(f)   # here it will return csvwriter object

# studentid = int(input("Enter student id:- "))
# rollno = int(input("Enter your roll number:- "))
# name = input("Enter your name:- ")
# mobileno = int(input("Enter your mobileno:- "))

# a.writerow([studentid,rollno,name,mobileno])

# print("Student record has save")

# f.close()


# ===============================================================
# Q12. Student Marks and Percentage
# ===============================================================

# import csv

# f = open("student2.csv","a",newline="")

# a = csv.writer(f)   # here it will return csvwriter object

# studentid = int(input("Enter student id:- "))
# name = input("Enter your name:- ")
# rollno = int(input("Enter your roll number:- "))
# mobileno = int(input("Enter your mobileno:- "))

# p1 = int(input("Enter your paper1 marks:- "))
# p2 = int(input("Enter your paper2 marks:- "))
# p3 = int(input("Enter your paper3 marks:- "))

# email = input("Enter you email:- ")

# if p1 >= 40 and p2 >=40 and p3 >= 40:
#     print("pass")
# else:
#     print("fail")

# total = p1 + p2 + p3

# percentage = total/3.0

# print("Total marks: ",total)
# print("Percentage: ",percentage)

# a.writerow([studentid,name,rollno,mobileno,p1,p2,p3,email])

# print("Student record has save")

# f.close()

# ===============================================================
# End of File Handling Practice
# ===============================================================
