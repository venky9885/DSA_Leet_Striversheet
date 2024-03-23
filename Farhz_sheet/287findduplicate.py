# https://leetcode.com/problems/find-the-duplicate-number/description/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # x = 1
        # print(x ^(2^2))
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i]^nums[i-1]  == 0):
                return nums[i]
        return 0

# Xor for same val  is  0
    # i,i+1 are same logic also we can apply