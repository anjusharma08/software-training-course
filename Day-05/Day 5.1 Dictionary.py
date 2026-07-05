#Q1
# mydic = {
#     101 : "prashant",
#     102 : "ashish",
#     "103" : "monini",  
#     "104" : "trivani",
#     101 : "ashish",
#     104 : "ashish",

# }
# print(mydic)
# print(type(mydic))
# # with the help of key we have to print values
# a = mydic[102]
# print(a)

#Q2
# #we replace old values by new value
# mydic[102] = "peter"
# print(mydic)

#Q3
#only print key x=0,1
# for x in mydic:
#     print(x)

#4
# # only print value x=0
# for x in mydic.values():
#     print(x)

# #5
# #printing key values both
# for x,y in mydic.items():
#     print(x,y)

# #6
# mydic["mobile_no"]=12455545
# print(mydic)

# #7
# mydic = {
#     101 : "prashant",
#     "professional" : "developer",
#     "empid" : 1010

# }
# mydic.pop(101)
# print(mydic)
# #pop() method remove pair by specific key name

# #8
# mydic = {
#     101 : "prashant",
#     "professional" : "developer",
#     "empid" : 1010

# }
# newdic = mydic.copy()
# print(newdic)

# #task

# #9  
# d={}
# def check_dict(d):
#     if not d:
#         print("Empty")
#     else:
#         print("Not Empty")

# check_dict(d)
    
#10
# mydict = {"A":50,"B":30,"c":70}
# highest_key=max(mydict,key=mydict.get)
# print(mydict[highest_key])

# print(highest_key)

# with fuction
# d= {"A":50,"B":30,"c":70}
# def max_key(d):
#     key = max(d, key = d.get)
#     print(key)
# max_key(d)

# #11 reverse the key-value pairs of a dic
# dic ={
#     "A":1,
#     "B":2,
#     "c":3
# }

#12
#13


