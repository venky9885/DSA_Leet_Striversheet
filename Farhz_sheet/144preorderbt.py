# preorder -root left right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        ans = []
        def r(ro):
            if(ro and ro.val != 'null' ):
                ans.append(ro.val)
                print(ro.val)
            if(ro and ro.left):
                r(ro.left)
            if(ro and ro.right):
                r(ro.right)
        r(root)
        return  ans

        