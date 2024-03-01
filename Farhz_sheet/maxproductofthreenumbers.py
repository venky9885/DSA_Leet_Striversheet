# If all the values are negative :  ( -5 -4 -3 -2 -1 )

# -5  -4  -3  -2  -1
# |____|
#   |-- These 2 values make a POSITIVE LARGE VALUE of 20 than other negative values
#       As we want maximum product, we will do 20 * -1 = -20  (20 * -2 = -40 < -20)

#   SO we return nums[0] * nums[1] * nums[last index]

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ar = sorted(nums)
        return max(ar[-1]*ar[-2]*ar[-3],ar[0]*ar[1]*ar[-1])
        
