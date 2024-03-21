# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# easy
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        re = []

        def preord(root):
            nonlocal re

            if(not root):
                return
            re.append(root.val)
            preord(root.left)
            preord(root.right)
        preord(root)
        if(not root):
            return
        # make left none otherwise all will come as repated
        root.left = None
        temp = root
        # start from 1 beacuse already root has value
        for i in re[1:]:
            temp.right = TreeNode(i)
            # after assigning move pointer
            temp = temp.right

        """
        Do not return anything, modify root in-place instead.
        """
