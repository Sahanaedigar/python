def fib(n):
    if(n==0 or n==1): return n

    return fib(n-1)+fib(n-2)


n=5
print(fib(n))


'''
0,1,1,2,3,5...
'''