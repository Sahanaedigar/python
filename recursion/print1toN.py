starts=1
def func(num):
    global starts
    if(starts>num):
        return
    print(starts)
    starts=starts+1
    func(num)



'''
easy way to print from 1-N
     print(starts)
     func(starts+1,num)
'''

func(10)