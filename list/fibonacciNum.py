# first=0
# second=1
# n=6

# for i in range(2,n+1):
#     third=second+first
#     first=second
#     second=third

# print(third)


previous_number = 0
current_number = 1
position = 6  # Position in Fibonacci sequence to find

for index in range(2, position + 1):
    next_number = previous_number + current_number
    previous_number = current_number
    current_number = next_number

print(f"The {position}th Fibonacci number is:", next_number)

'''
The Fibonacci sequence is defined as:

F(n)=F(n−1)+F(n−2)

With base cases:

F(0)=0,F(1)=1

Explanation of Variable Names:
previous_number: Represents the (n-2)th Fibonacci number

current_number: Represents the (n-1)th Fibonacci number

next_number: Represents the nth Fibonacci number

position: The target index (e.g., 6th Fibonacci number)

index: Loop counter (not directly used in calculation)

'''