#1 linear search
# def linearSearch(array,target):
#     for i in range(len(array)): #i=0
#         if array[i] == target: #7 == 7
#             return i
#     return -1

# array = [1,2,3,4,5,6,7,8,9]
# target = 7
# result = linearSearch(array, target) #calling function
# if result != -1:
#     print("Element found at index no = ",result)
# else:
#     print("Element not found")

#2st task 
array = [5,3,9,2,8]

def linerSearch(array):

    minimum  = array[0]
    maximum  = array[0]

    for i in range(len(array)):
        if array[i] < minimum:
            minimum = array[i]
        if array[i] > maximum:
            minimum = array[i]

    print("Minimum",minimum)
    print("Maximum",maximum)

linerSearch(array)

#3nd task Find the majority element
  


        

            