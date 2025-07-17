'''
word.startswith(K): Checks if word starts with the character stored in K without any case modification.
Only the words that exactly match the case of K will be included in the result.
'''

a = ["Kite", "Apple", "King", "Banana", "Kangaroo", "cat"]
cond='K'
res=[]
for i in a:
    if i.startswith(cond):
        res.append(i)
# print(res)

res=[x for x in a if x.startswith(cond)]
print(res)