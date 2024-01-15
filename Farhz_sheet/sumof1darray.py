class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0;l = []
        for i in range(len(nums)):
            s+=nums[i]
            l.append(s)
        return l


Runtime
# 45
# ms
# Beats
# 58.64%
# of users with Python3
# Memory
# 17.41
# MB
# Beats
# 29.52%
# of users with Python3
