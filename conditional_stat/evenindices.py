'''Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print
 characters of a string at even indices.'''

def evenindices(inputstr):
    lst=len(inputstr)
    for i in range(lst):
        if i%2==0:
            print(inputstr[i]) #strings letter can be print using index

ip=input()
evenindices(ip) 

NAME='sahana'
print(NAME[0])

