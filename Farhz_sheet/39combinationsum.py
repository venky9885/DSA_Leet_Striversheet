# https://leetcode.com/problems/combination-sum/description/

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def btr(arr, axp, tg, i):
            
            if sum(axp) == tg:
                return [axp]  
    
            elif sum(axp) > tg or i >= len(arr):
                return []  
            
            # here we will think why not incremented answer is we are reusing existing one
            include = btr(arr, axp + [arr[i]], tg, i)
            
            exclude = btr(arr, axp, tg, i+1)
            
            return include + exclude

        return btr(candidates, [], target, 0)
    

#  1 2 3
#   1
    # 1(reusing the same 1 for purspose of sum so adding the same and dont increment index)
