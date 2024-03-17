class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        pref = 1
        suff = 1
        n = len(nums)
        # we will iteratere from front and end update max
        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref = pref * nums[i]
            suff = suff * nums[n-i-1]
            ans = max(ans, pref, suff)
        return ans
# neetcode solution below
# class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if(n == 0):
                curMax, curMin = 1, 1
                continue
            tmp = curMax*n
            curMax = max(tmp, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res
