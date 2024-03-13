# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#dead easy
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def f(root):
            nonlocal sm
            if(not root):
                return
            if( low <= root.val <= high):
                sm+=root.val
            f(root.left)
            f(root.right)
        sm = 0
        f(root)
        return sm
        
