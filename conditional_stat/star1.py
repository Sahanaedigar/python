def printstar(row):
    for i in range (1,row+1):
        print(4*"* ")
# printstar(3)
'''
* * * * 
* * * *
* * * *
'''

# pattern--2
def printstar(row):
    for i in range (1,row+1):
        print(i*"* ")

# printstar(4)
'''
* 
* *
* * *
* * * *
'''

#pattern-3 inverted triangle
def printstar(row):
    for i in range(row, 0, -1): #start,end(end point not included), step(here decrease by 1)
        print(i*"* ")
# printstar(4)
'''
* * * * 
* * *
* *
*
'''
# pattern 4
def trianglepat(row):
    for i in range(1,row+1):
        print(i*'* ')
    for j in range(row,0,-1):
        print(j*'* ')

# trianglepat(4)
'''
* 
* *
* * *
* * * *
* * * *
* * *
* *
*
'''
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)