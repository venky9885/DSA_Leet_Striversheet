class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxSum = nums[0]
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            mxSum = max(curSum,mxSum)
        return mxSum



# Runtime
# Details
# 565ms
# Beats 82.88%of users with Python3
# Memory
# Details
# 31.72MB
# Beats 23.75%of users with Python3