#without dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ms = ''
        ml = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t = s[i:j] 
                if( t == t[::-1] and len(t) > ml):
                    ms = t
                    ml = len(t)
                #this will help to optimize the code
                if(ml == len(s)):
                    break
        return ms

        
#with dp
class Solution:
    def longestPalindrome(self, s: str) -> str:

        N = len(s)
        dp = [[False] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = True
            res = s[i]
            max_len = 1
        
        for L in range(2, N+1):
            for i in range(N-L+1):    
                j = i + L -1
                if s[i] == s[j] and (L == 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if L > max_len:
                        max_len = L
                        res = s[i: j+1]
        return res
