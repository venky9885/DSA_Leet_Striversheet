# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(nums.count(0) == 1):
            prod = 1
            for i in nums:
                if(i == 0):
                    continue
                prod *=i
            res = []
        
            for i in nums:
                if(i == 0):
                    res.append(prod)
                    continue
                res.append(0)
            return res
        elif(nums.count(0) > 1):
            return [0]*len(nums)
        else:
            prod = 1
            for i in nums:
                prod *=i
            res = []
        
            for i in nums:
                res.append(int(prod/i))
            return res
    