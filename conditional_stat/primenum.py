def checkprime(num):
    for i in range (2,num):
        if num%i==0:
           return "not prime"
    
    return "prime"



num=int(input())
print(checkprime(num))