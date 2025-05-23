def sumofnaturalnumbers(num):
    sum=0
    if num>0:
        for i in range(1,num+1):
            sum=sum+i
            for j in range(1,i+1):
                
                print(j,end=' ')
            print()
    print(sum)

num=int(input())
sumofnaturalnumbers(num)