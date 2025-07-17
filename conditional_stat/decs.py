def printindecreasingorder(num):  #using list
    # lst=[]
    # for i in range(num,0,-1):
    #     lst.append(i)
    # return lst

    while(num):      #using while statement
        print (num,'')
        num=num-1


num=int(input())
printindecreasingorder(num)

