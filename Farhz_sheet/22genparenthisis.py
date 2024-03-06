class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #a simple one using recursion
        #The idea is to add ')' only after valid '('
        # We use two integer variables left & right to see how many '(' & ')' are in the current string
        # If left < n then we can add '(' to the current string
        # If right < left then we can add ')' to the current string
        def dfs(l,r,s):
            if(len(s) == n*2):
                res.append(s)
                return
            if( l < n):
                dfs(l+1,r,s+'(')
            if(r < l):
                dfs(l,r+1,s+')')
        res = []
        dfs(0,0,'')
        return res
