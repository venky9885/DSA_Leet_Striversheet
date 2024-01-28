# https://leetcode.com/problems/permutations/



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permut(numsr,hp):
            # print(ind)
            
            if(not numsr):
                # print("huh",hp)
                res.append(hp.copy())
                return 
            # if(ind > len(nums)):
            #     return
            for i in range(len(numsr)):
                # print(nums,nums[:i]+nums[i+1:],hp,nums[i],hp+[nums[i]])
                permut(numsr[:i]+numsr[i+1:],hp+[numsr[i]])
        permut(nums,[])
        return (res)
    
# Take 1 number and except that pass remianing to recusrion as shown below
# In [1,2,3]
# take 1  in loop then 2  then 3
# rema [2,3],,,,[1,3],,,,,[1,2]
# take 2, in loop then 3
# rema [3] ,,,, [2]
