class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''

        for i in range(len(strs[0])):
            it  = strs[0][i]
            for j in range(len(strs)):
                if(i >= len(strs[j]) or strs[j][i] != it ):
                    return s
            s+=strs[0][i]
        return s
        

#easy to do , compare every string in loop