# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        df   = defaultdict(int)
        res = 0
        for i in time:
            i = i%60
            res  += df[(0-i)%60]
            df[i]+=1
        return res

        