def printsquareinrange(num):
    i=1
    for i in range(num):
        if i*i<=num:
            print(i*i)
num=int(input())
printsquareinrange(num)