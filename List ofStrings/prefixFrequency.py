a = ["geeks", "geeksforgeeks", "geeky", "geek", "apple", "banana"]

prefix='geeks'
count=0
# res=[x for x in a if x.startswith(prefix)]
# print(res)

res=[]
for x in a:
    if x.startswith(prefix):
        res.append(x)
        count+=1

print(res,count)

