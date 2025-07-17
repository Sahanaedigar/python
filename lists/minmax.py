def minmaxinArray(lst):
    return min(lst), max(lst)

# n = int(input("Enter the number of elements: "))
lst = [7, 1, 2, 4]

# for i in range(n):
#     num = int(input(f"Enter element {i+1}: "))
#     lst.append(num)
# lst.sort()
# minimum, maximum = minmaxinArray(lst)
print(lst)
# print("Minimum:", minimum)
# print("Maximum:", maximum)
# print(lst[1])

#finding second largest num
max1=max2=float('-inf')
for i in lst:
    if max1>i:
        max2=max1
        max1=i
    elif i > max2 and i != max1:
        max2=i

print(max1)