def bubbleSort(arr):
    for i in range ((len(arr)-1)):
        isswapped=False
        for j in range ((len(arr)-1)-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                isswapped=True
        if isswapped==False:
            print("given sorted array")
            break
    return arr


arr=[1,2,3,4]
print(bubbleSort(arr))