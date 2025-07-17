a = [1, None, 3, None, 5, 0]
res=[]

for i in a:
    if i is not None:
        res.append(i)
print(res)