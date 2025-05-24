
'''
check the lists are identical'''

a=[1,7,6]
b=[1,6,7]
flag=True
if len(a)!=len(b):
    flag=False
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            flag=False
            break
print(flag)  


'''
check the elements of the lists are same
'''
a=[1,7,6]
b=[1,6,7]
a.sort()
b.sort()
flag=True
if len(a)!=len(b):
    flag=False

else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            flag=False
            break
print(flag)  


print(a.pop())
print(a)
