# its easy problem

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        # count the difference for every lement les than right index and store difference in dp then return max
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right]-nums[left])] = dp.get((left, nums[right]-nums[left]), 1)+1
        return max(dp.values())
