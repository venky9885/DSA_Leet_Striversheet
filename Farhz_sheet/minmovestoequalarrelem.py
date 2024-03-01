class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # sum(nums)-(len(nums) * min(nums))
        m = min(nums)
        return sum(num-m for num in nums)
        
