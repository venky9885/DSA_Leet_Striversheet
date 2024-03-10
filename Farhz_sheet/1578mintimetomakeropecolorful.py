class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(1, len(colors)):
            if(colors[i] == colors[i-1]):
                res += min(neededTime[i], neededTime[i-1])
                # here this is importnt step we will forgot
                # after removing smallest ine you only have big color remain
                # instead of removing small from array update the value as max from i,i-1,so it will be forwarded
                neededTime[i] = max(neededTime[i], neededTime[i-1])

        return res
