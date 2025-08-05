# Node class
class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.next = None  # stores reference to the next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # head of the list (first node)

    def addAtHead(self, val: int) -> None:
        mynode = Node(val)         # create a new node
        mynode.next = self.head    # point new node to current head
        self.head = mynode         # move head to new node
        self.size += 1             # increase size

    def addAtTail(self, val: int) -> None:
        mynode = Node(val)         # create new node

        if self.head is None:      # if list is empty
            self.head = mynode     # new node becomes head
        else:
            curr = self.head
            while curr.next is not None:  # go to last node
                curr = curr.next
            curr.next = mynode     # connect last node to new node
        self.size += 1





'''
Node class:
Each node is an object with:

data: stores actual value

next: pointer to the next node (or None if it's the last)

LinkedList class:
head: starts as None (empty list)
'''