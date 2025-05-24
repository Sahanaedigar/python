a = [-10, 15, 0, 20, -5, 30, -2,-2]
positivecount=0
negativecount=0
a.sort()
for i in a:
    if i>=0:
        positivecount+=1
        print(i,"is positive number")
    else:
        negativecount+=1
        print(i, "is negative number")

print(positivecount ,negativecount)
newlst=set(a)
print(newlst)

# remove multiple element from the list
# res=[]
rem=[0,30,-2]
# for i in a:
#     if i not in rem:
#         res.append(i)
# print(res)

b=list(filter(lambda x:x not in rem,a))
print(b)
