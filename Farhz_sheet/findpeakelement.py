#this is perfect one with binary sol
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid=(left+right)>>1
            if (mid==0 or nums[mid]>=nums[mid-1] ) and (mid==len(nums)-1 or nums[mid]>=nums[mid+1]) :
                return mid
            elif nums[mid]<=nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1
#this does not satisfy question mentioned 0logn
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        it = 0
        #for len 1
        if(len(nums) == 1):
            return 0
        #for len 2
        if(len(nums) == 2):
            return 1 if(nums[1] > nums[0]) else 0
        #for len 1
        for i in range(1,len(nums)-1):
            if(nums[i-1] < nums[i] and nums[i] > nums[i+1]):
                # it = nums
                return i
        #for ex like  [1,2,3] then 3 is peak because there is no right
        if(nums[-2] < nums[-1]):
            return len(nums)-1
        return it
    

#it is easy only