# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #here itsimple if we will maintain mx which must be greater than its values
        #also update it when  mx=max(mx,node.val)
        def f(node,mx):
            if(not node):
                return 0
            if(node.val >= mx):
                cnt = 1
            else:
                cnt = 0
            mx=max(mx,node.val)
            cnt+=f(node.left,mx)
            cnt+=f(node.right,mx)
            return cnt
        return f(root,root.val)



        
