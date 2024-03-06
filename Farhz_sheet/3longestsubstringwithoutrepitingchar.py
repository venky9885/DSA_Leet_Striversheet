#check for expln https://youtu.be/pY2dYa1m2VM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we will store all chars with latest index
        # if we find character reapeating we will move left pointer to repchar + 1
        #and also checking the length by r-l+1
        seen = {}
        l,mx =0,0
        for r in range(len(s)):
            #if it is seen and index is greater then update left pointer 
            if s[r] in seen and seen[s[r]] >= l:
                # seen[s[r]] = r
                l = seen[s[r]]+1
            #else check length because its unique
            else:
                mx = max(mx,r-l+1)
            #update the char index at end
            seen[s[r]] = r
        return mx
        
