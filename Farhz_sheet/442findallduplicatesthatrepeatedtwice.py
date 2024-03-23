# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        res = set()
        i = 1
        while(i < len(nums)):
            print(nums[i] ^ nums[i-1])
            if((nums[i] ^ nums[i-1]) == 0 ):
                res.add(nums[i])
            i+=1
        print(res)
        return list(res)
        