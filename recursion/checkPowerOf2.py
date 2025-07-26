def CheckTheNumberIsPowerOfTwo(num):
    if num==1 :return True
    elif num ==0 or num % 2 != 0:
      return False

    return CheckTheNumberIsPowerOfTwo(num/2)


num=0
print(CheckTheNumberIsPowerOfTwo(num))
