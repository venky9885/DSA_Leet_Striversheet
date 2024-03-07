class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        for i in strs:
            t = ''.join(sorted(i))

            if(t in hs):
                hs[t].append(i)
            else:
                hs[t] = [i]
        r = []
        for i in hs:
            r.append(hs[i])
        return r


        