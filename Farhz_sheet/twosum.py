# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lg =  len(nums)
        hs = {}
        for i in range(lg):
            hs[nums[i]] = i
        for j in range(lg):
            rem =  target -nums[j]
            if(rem in hs and j != hs[rem]):
                return [j,hs[rem]]
        return []

        # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j] == target):
        #             return [i,j]
        