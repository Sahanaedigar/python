nums=[0,1,0,3,12]
i=0
while(i<len(nums)):
    if nums[i]==0:
        temp=nums[i]
        nums[i]=nums[i+1]
        nums[i+1]=temp
        i=i+1
    else:
        i=i+1

print(nums)