def factorialOfNum(num):
    if num==1 or num==0:return 1
    return num*factorialOfNum(num-1)
num=0
print(factorialOfNum(num))