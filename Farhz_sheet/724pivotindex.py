class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(sum(nums[0:i])-sum(nums[i+1:]) == 0):
                return i

        return -1
#! from internet
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         right = sum(nums)
#         left = 0

#         for i in range(len(nums)):
#             right -= nums[i]
#             if left == right:
#                 return i
#             left += nums[i]

#         return -1      
# Runtime
# 6150
# ms
# Beats
# 9.12%
# of users with Python3
# Memory
# 18.62
# MB
# Beats
# 10.34%
# of users with Python3