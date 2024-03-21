# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# generate all possib trees and return in list
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(left, right):
            if (left == right):
                return [TreeNode(left)]
            # here bst rule fails
            if (left > right):
                return [None]
            re = []
            for val in range(left, right+1):
                for leftTree in gen(left, val-1):
                    # here wetake val for root so we start from val+1
                    for rightTree in gen(val + 1, right):
                        re.append(TreeNode(val, leftTree, rightTree))
            return re

        return gen(1, n)
