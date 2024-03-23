# https://leetcode.com/problems/subsets-ii/description/



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subs(arr,hp,i):
            # print(i,len(nums))
            if(i == len(nums)):
                if(hp not in res):
                    res.append(hp.copy())
                return 
            # print(arr,hp+[nums[i]],i+1)
            subs(arr,hp+[nums[i]],i+1)

            subs(arr,hp,i+1)
        subs(nums,[],0)
        # print(res)
        return res
        
#same as subsets but  check same copy is not present
    
# The above Solution is not much optimal below is optimal
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, stack = [], []

        def backtrack(i):
            if i >= len(nums):
                output.append(stack.copy())
                return
            
            stack.append(nums[i])
            backtrack(i+1)

            stack.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1)
        
        backtrack(0)
        return output
    
#another similar
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, res):
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]], res)
        
        nums.sort()
        res = []
        dfs(0, [], res)
        return res