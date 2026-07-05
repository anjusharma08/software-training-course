#1 FILE HANDLINF :- whenever you want to use/strore in future for future perpose so we use the file handling 
# f = open("myfile.text","w")
# print("Name of file : ",f.name)
# print("file mode : ",f.mode)
# print("readable : ",f.readable())
# print("writeable : ",f.writable())
# print("file closed : ",f.name)
# f.close()
# print("file closed : ",f.closed)

# #2  
# f = open("myfile.text","w")
# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Nashik is a smart city")
# f.write("\n Mumbai is a smart city")
# f.close()
# print("file operation is done")

# #3 override
# f = open("myfile.text","w")
# f.write("\n Pune is a smart city")
# f.close()
# print("file operation is done")

#4 append
# f = open("myfile.text","a")
# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Nashik is a smart city")
# f.write("\n Mumbai is a smart city")
# f.write("\n Indore is a smart city ")
# f.close()
# print("file operation is done")

#5 inserting list
# f = open("myfile.text","w")
# mylist=["prashant"," ","mahesh"," ","suresh"," "]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")

#6 reading data from a file
# f = open("myfile.text","r")
# print((f.read()))
# f.close()

#7 properties of file object 
# with open ("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("file closed : ",f.closed)
# print("file closed : ",f.closed)

#8 
# with open("myfile.txt","r") as f :
#     content = f.read()
#     print(content)

#9 take image
# f1 = open("image.jpeg","rb")
# f2 = open("image1.jpg","wb")
# data = f1.read()
# f2.write(data)

#10 csv model
# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f) #here it will return csvwriter object
# #a.writerow(["studentID","rollno","name","mobileno"])

#11
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

#12
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

# total = p1 + p2 +p3
# percentage = total/3.0

# print("Total marks: ",total)
# print("Percentage: ",percentage)

# a.writerow([studentid,name,rollno,mobileno,p1,p2,p3,email])
# print("Student record has save")

# f.close()



