def revsString(inputstr):
    str1=[]
    start=len(inputstr)
    for i in range(start-1,0,-1):
        str1.append(inputstr[i])
    return str1


inputstring=['s','a','h','a','n','a']
print(revsString(inputstring))


'''
If you're reversing a list of length n, always do:
range(n - 1, -1, -1)'''