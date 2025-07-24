

def sumOfArray(arr):
    i=0
    if i>=len(arr):return arr[i]
    sumation=0
    sumation=sumation+arr[i]


    return sumation+sumOfArray(arr[i+1])

arr=[1,2,3,4,5]
print(sumOfArray(arr))