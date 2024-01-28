# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

def uni(ar):
    return len(ar) == len(set(ar))
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mxu = 0
        def btk(i,ctr):
            #to avoid local bound error
            nonlocal mxu
            if(uni(ctr)):
                mxu = max(mxu,len(ctr))
                # print(len(ctr))
                # return
            if(i > len(arr)-1 or (not uni(ctr))):
                return   
            btk(i+1,ctr+arr[i])
            btk(i+1,ctr)
        btk(0,"")
        print(mxu)
        return mxu
                

# Code is written using backtracking,with 30% eff
# make sure check videos with dp and btk also
# https://www.youtube.com/watch?v=d4SPuvkaeoo

#DP solution
# dp[i + 1] = all substrings with unique characters ending at s[i].
# similar to LIS problem, enumerate all dp[j], j < i and check for uniqueness.
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = defaultdict(list)
        dp[0].append("")
        ans = 0
        for i, s in enumerate(arr):
            set_s = set(s)
            if len(set_s) != len(s):
                continue
            for j in range(i + 1):
                for v in dp[j]:
                    isExist = any(c in set_s for c in v)
                    if not isExist:
                        dp[i + 1].append(v + s)
            ans = max(ans, len(max(dp[i + 1], key=len)))
        return ans