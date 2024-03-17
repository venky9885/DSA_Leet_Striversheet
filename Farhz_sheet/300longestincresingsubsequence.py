# see dfs approach in https://www.youtube.com/watch?v=cjWnW0hdF1Y then see the dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1]*n  # (we use 1 because everypoint is lenght 1 subaray)
        # we do bottom up from end to start from end to till 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if(nums[j] > nums[i]):
                    l[i] = max(l[i], 1+l[j])
        return max(l)
