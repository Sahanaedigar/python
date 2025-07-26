

def sumOfArray(arr,i=0):
   
    if i==len(arr):return 0
    return arr[i]+sumOfArray(arr,i+1)

arr=[0,1]
print(sumOfArray(arr))