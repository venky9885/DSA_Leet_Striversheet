#easy read questoin clear and do it

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t1 = [0]*(n+1)
        t2 = [0]*(n+1)
        for i in trust:
            t1[i[0]]+=1
            t2[i[1]]+=1
        for i in range(1, n + 1):
            if(t2[i] == n-1  and  t1[i] == 0):
                return i
        return -1

        
        
        
