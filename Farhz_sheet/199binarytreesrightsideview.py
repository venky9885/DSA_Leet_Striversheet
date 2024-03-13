# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(list)
        def f(root,l):
            if(not root):
                return 
            d[l].append(root.val)
            f(root.left,l+1)
            f(root.right,l+1)
        f(root,0)
        s = []
        for i in d.values():
            s.append(i[-1])
        return s

        
