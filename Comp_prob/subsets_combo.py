from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if start == len(nums):
                subsets.append(path)
                return
            # Exclude current element
            backtrack(start + 1, path)
            # Include current element
            backtrack(start + 1, path + [nums[start]])
        
        subsets = []
        backtrack(0, [])
        return subsets


# from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, subsets):
            subsets.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path, subsets)
                path.pop()

        subsets = []
        backtrack(0, [], subsets)
        return subsets

# Example usage:
nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))


#                 []
#                / \
#               /   \
#              /     \
#           [1]       []
#           / \      / \
#          /   \    /   \
#     [1,2]  [1]  [2]   []
#     / \    /      |
#    /   \  /       |
# [1,2,3][1,3]  [2,3] 
