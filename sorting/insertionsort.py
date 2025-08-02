
def insertion_Sort(arr):
    # min=float('inf')

    for i in range(len(arr)-1):
        min=arr[i]
        for j in range(i+1,len(arr)-1):
            if arr[j]<min:
                min=j
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
       



arr=[3,4,1,8,2]
print(insertion_Sort(arr))