# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#! post order  left right root

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def r(ro):

            if(ro and ro.left):
                r(ro.left)
            if(ro and ro.right):
                r(ro.right)
            if(ro and ro.val != 'null'):
                # r(ro.left)
                ans.append(ro.val)
                print(ro.val)
        r(root)
        return ans

        