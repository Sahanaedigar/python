lst = [7, 10, 2, 4]
lst2 = [7,5, 10, 2, 4]
# maxpos = minpos = -1

# max=float('-inf')
# min=float('inf')

# for i,j in enumerate(lst):
#     if j>max:
#         max=j
#         maxpos=i

#     if j<min:
#         min=j
#         minpos=i

# print(maxpos)
# print(minpos)


lst.sort()
maxpos=len(lst)-1
print("minimum position is 0 ",lst[0])
print(f"maximum position is {maxpos} ",lst[len(lst)-1])
print(lst+lst2)
print(lst and lst2)   