# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        m = []
        def f(root):
            nonlocal m
            if(not root):
                
                return
            m.append(root.val)

            f(root.left)

            f(root.right)
        f(root)
        m.sort()
        mx = float(inf)
        for i in range(1,len(m)):
            mx = min(mx,abs(m[i] - m[i-1]))
        return mx
            
            
