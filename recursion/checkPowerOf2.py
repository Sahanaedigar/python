def CheckTheNumberIsPowerOfTwo(num):
    if num==1 or num==0:return True
    elif num < 1 or num % 2 != 0:
      return False

    return CheckTheNumberIsPowerOfTwo(num/2)


num=0
print(CheckTheNumberIsPowerOfTwo(num))