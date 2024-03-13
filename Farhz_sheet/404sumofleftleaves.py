# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#easy done on own
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        re = []
        def f(root,l):
            nonlocal re
            if(not root ):
                return
            if(l == "L" and root.left is None and root.right is None):
                re.append(root.val)
            f(root.left,"L")
            f(root.right,"R")

        f(root,"U")
        print(re)
        return sum(re)
            
