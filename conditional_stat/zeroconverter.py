def zeroconverter(num):
    if num==0:
        print("already zero")
    elif num<0:
        while(num<=0):
            print(num)
            num=num+1
    else:
        while num >= 0:
            print(num)
            num -= 1
        
        
num=int(input())
zeroconverter(num)