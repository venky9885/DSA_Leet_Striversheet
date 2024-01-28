# https://leetcode.com/problems/jump-game-ii/description/
#dp solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        


        # # DP this is solution for jumpgame not for jump game 2 
        # dp  = [0 for _ in range(n)]


        # dp[0] =  1

        # for i in range(n):
        #     if(dp[i]):
        #         for j in range(1,nums[i]+1):
        #             # i+j
        #             if(i+j < n):
        #                 dp[i+j] = True
        #             if(i+j == n-1):
        #                 return True
        # return False
# DP solution in range 0 to n
# intially set true, and set the reachable position true
#traverse it by storing in memo
    



#greedy solution
#for better explanation watch neetcode yt video     
class Solution:
  def jump(self, nums: List[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i])
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level

    return ans        
