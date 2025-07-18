

def remDuplicates(arr):
    i=1
    while i<len(arr):
        if arr[i]==arr[i-1]:
            arr.remove(i)
        else:
            i=i+1
    return arr,len(arr)

arr=[1,1,1,2,3,5]

print(remDuplicates(arr))