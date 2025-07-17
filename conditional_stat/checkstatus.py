'''
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
'''

def checkstatus(a, b, flag):
    if ((a >= 0 and b < 0) or (a < 0 and b >= 0)) and flag == False:
        return True
    elif a < 0 and b < 0 and flag == True:
        return True
    else:
        return False

# Input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
flag_input = input("Enter flag (True/False): ").strip()

# Convert string input to actual boolean
flag = flag_input.lower() == 'true'

# Output
print(checkstatus(a, b, flag))
