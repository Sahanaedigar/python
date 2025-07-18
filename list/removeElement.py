
def removeElements(nums,val):
    i=1
    while i<len(nums):
        if nums[i]==val:
            nums.pop(i)
        else:
            i=i+1
    return len(nums),nums

    







nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElements(nums,val))

