# sr =  False

# @lru_cache

    # print("waste")
    # return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sr = False
        @lru_cache
        def wr(i):
            nonlocal sr
            if(i ==  len(s)):
                sr = True
                return True
            for w in wordDict:
                if(s[i:].startswith(w)):
                    wr(i+len(w))
        wr(0)
        return sr
        

# Match dict  word usng for loop
# @cache for optimization