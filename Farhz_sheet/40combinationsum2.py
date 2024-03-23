
#this below solution is non optimal (Brute Frc) throws TLE


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def btk(i,hp):
            if( sum(hp) == target and hp not in res):
                res.append(hp.copy())
                return 
            if(sum(hp)>target or i >= len(candidates)):
                return

            btk(i+1,hp+[candidates[i]])

            btk(i+1,hp)

            # return res1+res2
        btk(0,[])
        print(res)
        return res
# this similar like subsets 2 as said by md Fraz  and also watch neet code with below link
    # https://www.youtube.com/watch?v=rSA3t6BDDwg
    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res