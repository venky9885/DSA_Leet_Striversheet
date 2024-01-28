# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])
        
        min_sum = subarray_sum
        for i in range(remaining_length, n):
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
        # l = 0;r = len(cardPoints)-k
        # curs = sum(cardPoints)
        # mi = float('-inf')
        # while(l < k):
        #     cur = curs-sum(cardPoints[l:r])
        #     mi = max(mi,cur)
        #     l+=1
        #     r+=1
        # return mi
            

#for better explantaion see neet code  yt video from below link
    # https://www.youtube.com/watch?v=TsA4vbtfCvo
    # [1,2,3,4,5,6,7]
    # |______||__k__| this is k required on both sides just move it and
    #  dont compute sum every time instaed remove last elem sum and add new