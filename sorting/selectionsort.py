def slectionSort(arr):
    for i in range(1,len(arr)):

        key=arr[i]
        j=i-1
        while arr[j]>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
    return arr

arr=[3,4,1,8,2,0,0]
print(slectionSort(arr))