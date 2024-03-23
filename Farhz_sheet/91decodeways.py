# Memo
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def drc(s):
            if(len(s) == 0):
                return 1
            if(s[0] == '0'):
                return 0
            if(s in memo):
                return memo[s]
            s1 = s[0]
            s2 = s[:2]
            c = 0
            c+=drc(s[1:])
            if(len(s2) >= 2 and 1 <= int(s2) <= 26):
                c+= drc(s[2:])
            memo[s] = c
            return c
        return drc(s)

        
