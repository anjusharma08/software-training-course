# ===============================================================
# Day 05 – Python Queue Practice
# ===============================================================

# Topics:
# 1. Queue
# 2. isFull()
# 3. isEmpty()
# 4. enQueue()
# 5. display()
# 6. deQueue()
# 7. Frontpeek
# 8. Delete Queue
# 9. Menu Driven Queue Program

# ===============================================================
# Practice Question
# ===============================================================

import sys

class Queue:

    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue.pop(0))

    def frontpeek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue[0])

    def deleteQueue(self):
        self.myQueue = None
        print("Queue is deleted!")


size = int(input("Enter the size of Queue : "))

quObj = Queue(size)

while True:

    print("1. enQueue")
    print("2. display")
    print("3. deQueue")
    print("4. Frontpeek")
    print("5. Delete Queue")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to add in queue:- "))
        quObj.enQueue(value)

    elif choice == 2:
        quObj.display()

    elif choice == 3:
        quObj.deQueue()

    elif choice == 4:
        quObj.frontpeek()

    elif choice == 5:
        quObj.deleteQueue()

    elif choice == 6:
        sys.exit()

# ===============================================================
# End of Queue Practice
# ===============================================================
