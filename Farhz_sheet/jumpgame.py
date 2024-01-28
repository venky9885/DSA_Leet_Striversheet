# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n  = len(nums)
        dp  = [False for _ in range(n)]


        dp[0] =  True

        for i in range(n):
            if(dp[i]):
                for j in range(1,nums[i]+1):
                    # i+j
                    if(i+j < n):
                        dp[i+j] = True
                    if(i+j == n-1):
                        return True
        return False


        #GReedy
        # goal =  len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     print(nums[i]+i,goal)
        #     if(i+nums[i]>=goal):
        #         goal = i
        # return True if (goal == 0) else False
        
#! check the neetcode yt for best explanation