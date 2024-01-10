class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        ln = len(nums)

        i = 0
        j = ln-1


        while(i < j):
            print(nums.count(nums[i]),ln/2)
            if(nums.count(nums[i]) > ln/2):
                return nums[i]
            elif(nums.count(nums[j]) > ln/2):
                return nums[j]
            i+=1
            j-=1
        return 0



# Runtime
# Details
# 136ms
# Beats 88.97%of users with Python3
# Memory
# Details
# 18.98MB
# Beats 12.28%of users with Python3