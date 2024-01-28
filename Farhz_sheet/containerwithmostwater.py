# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = height
        
        i = 0
        j = len(x)-1
        mx = 0
        while(i < j):
            mx = max(min(x[i], x[j])*(j-i), mx)
            if(x[i] < x[j]):
                i += 1
            else:
                j -= 1
        print(mx)
        return mx
        # a  = 0
        # max  = 0
        # # l = []
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         a  = (j-i)*min(height[i],height[j])
        #         # print(a)
        #         if(a  > max):
        #             max  =  a
        #         # l.append(a)
        # return max
                
                
                
        
       # print(list(set(sorted(height))))
#2 pointer i and j move which ever less height