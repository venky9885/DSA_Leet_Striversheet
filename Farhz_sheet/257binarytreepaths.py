# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#easy done on own
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def f(root,pt):
            nonlocal res
            if(not root ):
                return
            
            if(not root.left and not root.right):
                res.append(pt+"->"+str(root.val))
            
            f(root.left ,pt+"->"+str(root.val))
            
            f(root.right,pt+"->"+str(root.val))
        l = []
        f(root,"")
        for i in res:
            l.append(i[2:])
        return l
        
