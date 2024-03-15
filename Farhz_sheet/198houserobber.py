# for beettr expln neetcode see https://www.youtube.com/watch?v=73r3KWiEvyk

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1,rob2,i,i+1]
        # here we skip one home and sum the alternative home and middile skipped home
        # then will be adding to the rob1 and rob2 respectively without violating adjacent home rule
        # the update rob1 by single step i.e rob2
        # so we return max from rob1 and rob2
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1, rob2)
    # this solution also so easy


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            # dp = [i-2,i-1,i] skippingg alternative
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]
