def printtriangle(n):
    for i in range(n+1):
        for j in range (i):
            print(i," ",end='')
        print()

# n=int(input())
# printtriangle(n)

def printtriangle2(n):
    for i in range(n+1):
        for j in range (i):
            print(j+1," ",end='')
        print()


# n=int(input())
# printtriangle2(n)


def invertedtriangle(n):
    for i in range(n+1,0,-1):
        for j in range (i):
            print(j+1," ",end='')
        print()

# n=int(input())
# invertedtriangle(n)

'''
      * 
    * * 
  * * * 
* * * * 
'''

def spaceAndStar(n):
    rows=n
    for i in range(n+1):
        print(' ' * (rows-i) + '* '*i)

# n=int(input())
# spaceAndStar(n)

'''
1
1 0
1 0 1
1 0 1 0'''

def zeroAndOnes(n):
    for i in range(1,n+1):
        for j in range (1,i+1):
           if j%2==1:print('1 ',end='')
           else:print('0 ',end='')
        print()    

# n=int(input())
# zeroAndOnes(n)

'''
1
0 1
0 1 0
1 0 1 0'''
rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        # Logic: alternate between 1 and 0, starting with 1 for odd rows, 0 for even rows
        print((i + j) % 2, end=" ")
    print()

# n=int(input())
# zeroAndOnes2(n)