class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadanes Algo
        #if elem less than zero make cur elem max
        #if all are postive let add it
        #if alreday sum is +ve and add negtve also ,because we need sub array
        #intialize both,with start element
        # maintain current max
        mx = nums[0];cur = nums[0]

        for i in range(1,len(nums)):
            if(cur < 0):
                cur  = 0
            cur+=nums[i]
            mx =  max(mx,cur)
        return mx
