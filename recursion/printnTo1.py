def func(num):
    if num==0:
        return
    
    print(num)
    num=num-1
    func(num)

func(10)