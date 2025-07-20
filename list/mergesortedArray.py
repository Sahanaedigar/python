nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# i=0
# while(i<len(nums1)):
#     if nums1[i]==0:
#         nums1.pop(i)
#     else:
#         i=i+1

# num3=nums1+nums2        
# num3.sort()
# print(num3)

'''leetcode-88'''
for i in range(n):
    nums1[m + i] = nums2[i]
nums1.sort()
print(nums1)