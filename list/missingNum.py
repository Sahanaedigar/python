nums = [9,6,4,2,3,5,7,0,1] #finding the missing num in the given list
nums.sort()
print(nums)
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]+1:  #value of next element (ex 2) is sum of value of 1st elemet and +1) as it is sorted 
        print(nums[i-1]+1)
        break

'''leetcode -268'''

#   def missingNumber(self, nums: List[int]) -> int:
#         n=len(nums)
#         sumofn=n*(n+1)//2
#         sumofList=sum(nums)
#         return sumofn-sumofList

