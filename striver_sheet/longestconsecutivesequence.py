class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n =  len(nums)
        if(n == 0):
            return 0
        mx,tg = 1,1
        if(n == 1):
            return 1
        l = 1
        while(l < n):
            print(l)
            if(nums[l-1] +1 == nums[l]):
                # print(mx,tg)
                mx+=1
                tg = max(mx,tg)
                print("tg",tg)
            else:
                # tg= max(mx,tg)
                mx = 1
            l+=1
        return tg
    

# Runtime
# 561
# ms
# Beats
# 42.77%
# of users with Python3
# Memory
# 34.27
# MB
# Beats
# 13.81%
# of users with Python3