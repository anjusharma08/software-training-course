# ===============================================================
# Day 07 – Python Linked List Practice
# ===============================================================

# Topics:
# 1. Node Creation
# 2. Linked List Creation
# 3. Connecting Nodes
# 4. Display Linked List

# ===============================================================
# Q1. Create and Display a Linked List
# ===============================================================

class Node:
    def __init__(self, value):
        self.data = value  # instance variable
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


linkedlist = LinkedList()

# Creating nodes

linkedlist.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Connecting nodes

linkedlist.head.next = second
second.next = third
third.next = fourth

# Display linked list

while linkedlist.head != None:
    print("|", linkedlist.head.data, "|", "->", end=" ")
    linkedlist.head = linkedlist.head.next

# ===============================================================
# End of Day 07 – Linked List Practice
# ===============================================================
