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
#DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #it is similar to kadanes just diffrence is that we maintain the max in array ,but in kadanes we maintain in a variable.it takes extra space and last we have to compute max
        # DP
        dp = [0]*len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],0)+nums[i]
        # print(dp)
        return max(dp)
