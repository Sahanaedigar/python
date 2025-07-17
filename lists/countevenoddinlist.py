lst=[7, 1, 2, 1,3,5,4]
evencount=0
oddcount=0
for i in lst:
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
# oddcount=len(lst)-evencount
print(evencount)
print(oddcount)
