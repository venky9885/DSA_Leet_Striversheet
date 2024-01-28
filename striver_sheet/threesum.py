class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if(i > 0 and nums[i] ==  nums[i-1]):
                continue
            l,r = i+1,len(nums)-1
            while(l < r):
                # print(nums[i],nums[l],nums[r])
                tsum =  nums[i]+nums[l]+nums[r]
                if(tsum  == 0):
                    res.append([ nums[i],nums[l],nums[r]])
                    l+=1
                    while( nums[l] == nums[l-1] and l < r):
                        l+=1
                    # r-=1
                elif(tsum < 0):
                    l+=1
                else:
                    r-=1
                
        # print(res)
        return res



# Runtime
# 714
# ms
# Beats
# 79.42%
# of users with Python3
# Memory
# 21.54
# MB
# Beats
# 26.95%
# of users with Python3