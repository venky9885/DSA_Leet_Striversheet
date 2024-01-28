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
            
        


#         Runtime
# Details
# 129ms
# Beats 81.25%of users with Python3
# Memory
# Details
# 22.00MB
# Beats 9.85%of users with Python3