class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[i]*nums[i])
        return sorted(res)
        

# Runtime
# 162
# ms
# Beats
# 78.24%
# of users with Python3
# Memory
# 19.35
# MB
# Beats
# 36.45%
# of users with Python3
