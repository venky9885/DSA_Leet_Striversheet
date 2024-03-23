# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/description/


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def calc(arr,h):
            
            arr.append(0)
            arr.append(h)
            mx = 0
            
            arr.sort()
            print(arr)
            for i in range(1,len(arr)):
                mx = max(arr[i]-arr[i-1],mx)
            print(arr,mx)
            return mx
        return (calc(horizontalCuts,h)*calc(verticalCuts,w)) % (7+(10**9))


        # it is simple calc all areas by adding start point 0  and end point
    # do this % (7+(10**9) because its given question
