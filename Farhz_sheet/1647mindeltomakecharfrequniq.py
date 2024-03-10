# watch neetcode if not understood
class Solution:
    def minDeletions(self, s: str) -> int:
        # here create unique set and if the frequency not in unique set dec it,if 0 ignore it
        ct = Counter(s)
        uni = set()
        a = 0
        # at last you only have unique in set freq
        for c, freq in ct.items():
            while(freq > 0 and freq in uni):
                freq -= 1
                a += 1
            uni.add(freq)
        return a
