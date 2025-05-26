a = [[1, 2], [], [3, 4], [], [5]]
# res = []

# for i in a:
#     if i:
#         res.append(i)

res=[ i for i in a if i ]
print(res)