#this is easiest one but some imp logic at  L11
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while(l<=r):
            m = (l+r)//2

            if(nums[m] == target):
                print(m)
                #L11
                t,s = m,m
                #here we use  0 < t but why not 0 <= t means t-1 here it is computed earlier same for another while loop nelow
                while(0 < t and  nums[t-1] == target ):
                    t-=1
                while( s < len(nums)-1 and nums[s+1] == target):
                    s+=1
                print(t,s)

                
                

                return [t,s]
            if(nums[l] <= target < nums[m]):
                r = m-1
            else:
                l = m+1
        return [-1,-1]
        