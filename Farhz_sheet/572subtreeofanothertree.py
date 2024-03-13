# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# this is easy one for bettr understanding https://www.youtube.com/watch?v=E36O5SWp-LE
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subtree root is null then return  tree
        if(not subRoot):
            return True
        if not root:
            return False
        if(self.isSameTree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # if subtree root is null then return  true

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        # if value of s and t must be true and if its sub roots are null then also true
        if(s and t and s.val == t.val):
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False
