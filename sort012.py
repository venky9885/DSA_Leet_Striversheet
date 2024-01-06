class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]>nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        

# Runtime
# Details
# 40ms
# Beats 63.17%of users with Python3
# Memory
# Details
# 17.48MB
# Beats 9.59%of users with Python3