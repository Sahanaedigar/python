def checkevenodd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    
num=int(input("enter the num: "))
res=checkevenodd(num)
print(res)