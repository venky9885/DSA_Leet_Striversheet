class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n =  len(nums)
        res = []

        for i in range(n-3):
            if( i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,n-2):
                if(j > i+1 and nums[j] == nums[j-1]):
                    continue
                l,r = j+1,n-1
                while(l < r):
                    ts = nums[i]+nums[j]+nums[l]+nums[r]
                    if(ts == target):
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
                        while(l < r and nums[r] == nums[r-1]):
                            r-=1
                    elif(ts < target):
                        l+=1
                    else:
                        r-=1
        return res
    



# Runtime
# 439
# ms
# Beats
# 71.38%
# of users with Python3
# Memory
# 17.28
# MB
# Beats
# 39.43%
# of users with Python3