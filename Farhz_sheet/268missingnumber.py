class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        
        return int(n*((n+1)/2)-sum(nums))
# XORing a number with itself always gives 0
#one more solution with XOR        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
