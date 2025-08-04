# Node class
class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.next = None  # stores reference to the next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # head of the list (first node)



'''
Node class:
Each node is an object with:

data: stores actual value

next: pointer to the next node (or None if it's the last)

LinkedList class:
head: starts as None (empty list)
'''