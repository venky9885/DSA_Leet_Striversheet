


#Below solution is Brute force throws TLE 
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # if(len(nums) == k):
        #     return []
        mem = {}
        
        med = 0
        # nums.sort()
        if(k%2 != 0):
            med =  (k+1)//2
        else:
            med = k//2
        res = []
        for i in range(len(nums)-k+1):
            if(k%2 != 0):
                res.append(sorted(nums[i:i+k])[med-1])
            else:
                ls = sorted(nums[i:i+k])
                res.append((ls[med-1]+ls[med])/2)
        print(res)
        return res