# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        op = [intervals[0]]
        for st,end in intervals[1:]:
            if(st <= op[-1][1]):
                op[-1][1] = max(end,op[-1][1])
            else:
                op.append([st,end])
        return op
            
        