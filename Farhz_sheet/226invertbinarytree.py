# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        # store in temp and swap it
        temp = root.left
        root.left = root.right
        root.right = temp
        # then got to depth of tree

        self.invertTree(root.left)

        self.invertTree(root.right)
        return root
