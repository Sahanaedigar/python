nums = [1,1,0,1,1,0,1,1,1,1]

currCount=0
maxCount=0

for i in range(len(nums)):
    if nums[i]==1:
        currCount+=1
    else:
        maxCount=currCount
        currCount=0
print(max(currCount,maxCount))

'''
prints consecutive 1's
check if it is one
if one increment currentcount
else
assign the currentcount(i.e num of 1"s till now to maxcount)
and currCount=0
print(max of currcount,maxcount)'''