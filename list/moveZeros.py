# '''
# bruteforce

# delete all zeros
# and adding zero at the end
# '''


# nums=[0,1,0,3,12]
# i=0
# originalsize=len(nums)
# size=len(nums)
# while (i<size):
#     if nums[i]==0:
        
#         nums.pop(i)
#         size-=1
#         print(nums,len(nums))
#     else:
#         i=i+1
# print(nums)

# addzeros=originalsize-size
# for j in range(addzeros):
#     nums.append(0)
# print(nums)




#efficiet way to print only non zero numbers
# nums = [0, 1, 0, 3, 12]
# nums = [x for x in nums if x != 0]
# print(nums)


nums=[0,1,0,3,12]
postiontoADDNonzeronumbers=0

for i in range(len(nums)):
    if nums[i]!=0:
        nums[postiontoADDNonzeronumbers]=nums[i]
        postiontoADDNonzeronumbers+=1

for i in range(postiontoADDNonzeronumbers,len(nums)):
    nums[i]=0
print(nums)