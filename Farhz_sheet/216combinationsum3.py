# https://leetcode.com/problems/combination-sum-iii/description/


res = []

def btk(i,k,hp,n):
    if(len(hp) == k and sum(hp) == n):
        res.append(hp.copy())
        return
    if(i > n or sum(hp) > n or i > 9):
        return


    btk(i+1,k,hp+[i],n)

    btk(i+1,k,hp,n)
    # btk

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res.clear()
        btk(1,k,[],n)
        print(res)
        return res
    

#Search better solution 
        