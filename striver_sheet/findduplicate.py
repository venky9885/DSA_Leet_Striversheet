class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for i in nums:
            if(i in l):
                return i
            else:
                l.add(i)

 

#  Accepted
# Editorial
# Solution
# Runtime
# Details
# 447ms
# Beats 98.86%of users with Python3
# Memory
# Details
# 33.53MB
# Beats 12.66%of users with Python3       