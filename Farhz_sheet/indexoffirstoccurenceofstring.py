class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if()
        h = len(haystack)
        n = len(needle)
        for i in range(h):
            if(haystack[i:i+n] == needle):
                return i
        return -1
        #its simple but set range h lengths not h-n