
#this problem is quite confusing and solved usaig binary search
#[4567 012] think this is array and find index of target
#for better understanding check neetcode video ,also watch graph
# https://www.youtube.com/watch?v=U8XENwh8Oy8
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r =0,len(nums)-1
        while( l <= r):
            m = (l+r)//2
            if(nums[m] == target):
                return m
            #left portion
            if(nums[l] <= nums[m]):
                #we use <=  because mid is already compared so for left we are comparing
                if(nums[l] <= target < nums[m]):
                    r = m -1
                else:
                    l = m+1
            #right portion
            else:
                #we use <=  because mid is already compared so for right[r] we are comparing
                if(nums[m] < target <= nums[r]):
                    l = m+1
                else:
                    r = m-1
        return -1

        
#this solution also works written smartly but not be accepted
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1