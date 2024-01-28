
# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def btk(i,hp):
            if( i  >  n):
                if len(hp)==k:
                    res.append(hp.copy())
                return 

            btk(i+1,hp+[i])

            btk(i+1,hp)
        btk(1,[])
        print(res)
        return res

# its normal like subsets but we will append to res when length == K