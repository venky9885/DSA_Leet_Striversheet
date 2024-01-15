class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j,c = 0,len(nums),0
        while( (i+c) < j):
            if(nums[i]==0):
                tp =  nums[i]
                nums.pop(i)
                nums.insert(j-1,0)
                c+=1
            else:
                i+=1




# Runtime
# 132
# ms
# Beats
# 78.44%
# of users with Python3
# Memory
# 18.66
# MB
# Beats
# 44.44%
# of users with Python3