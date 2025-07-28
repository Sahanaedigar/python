arr = [0, 1, 5, 7, 8, 9]
target=100
for i in range(len(arr)):
    if arr[i]==target:
        print(arr[i],i)
        break
else:
    print(-1)