# its easiest one
# just iterate through string and count for palindrome for odd type and even type
# for expln see https://www.youtube.com/watch?v=4RACzI5-du8
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.pal(s, i, i)
            res += self.pal(s, i, i+1)
        return res

    def pal(self, s, l, r):
        res = 0
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            res += 1
            l -= 1
            r += 1
        return res
