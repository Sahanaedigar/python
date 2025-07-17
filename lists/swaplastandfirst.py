my_list = [1, 2, 3, 4, 5]
a = [10, 20, 30, 40, 50]

# Interchange first and last elements
my_list[0], my_list[-1] = my_list[-1], my_list[0]
a[0], a[-2] = a[-2], a[0]
print(a)
# Print the modified list
print("List after swapping first and last elements:", my_list)