# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the problem tells to return nth indexed number from 1st index
        self.ct = 1
        self.ksm = None

        def hp(node):
            if(not node or self.ksm):
                return
            hp(node.left)
            print(self.ct)
            if(self.ct == k):
                self.ksm = node.val
                # return
            self.ct += 1
            hp(node.right)
        hp(root)

        return self.ksm
