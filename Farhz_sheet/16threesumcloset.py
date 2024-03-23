# https://leetcode.com/problems/3sum-closest/description/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tp = [];tg = []
        res  = 0
        l = 0;r =  len(nums)-1
        for i in range(len(nums)-2):
            l = i+1;r = len(nums)-1
            print(i,l,r)
            while(l < r):
                res = nums[i]+nums[l]+nums[r]
                tp.append(res)
                tg.append(abs(target-res))

                # print(res)
                if(res == target):
                    return target
                if(res > target):
                    r-=1
                else:
                    l+=1
        resind  = tg.index(min(tg))
        # print(tp,tg,min(tg))
        return tp[resind]

        
# similar to three sum
# return closest