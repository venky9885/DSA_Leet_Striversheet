class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s = list(s)[::-1]
        re = []
        for i in s:
            if(i is not ''):
                re.append(i)
        # print(s)
        return ' '.join(re)
# most easy
