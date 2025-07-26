def sumofN(num):
    if num==0:
        return 0
    # res=0
    # res=num+sumofN(num-1)
  
    return num+sumofN(num-1)
    
    

print(sumofN(5))

'''
return result → passes the value back to the previous function call.

In recursion, return is essential to chain the results back up the call stack.
'''