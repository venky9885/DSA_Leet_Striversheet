# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#its easy just merge the values after add  and give it by creating new node
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        t1 = root1
        t2 = root2
        if not t1 and not t2:
            return None
        v1 = t1.val if t1  else 0
        v2 = t2.val if t2  else 0 

        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(t1.left if t1 else None,t2.left if t2 else None)
        node.right = self.mergeTrees(t1.right if t1 else None,t2.right if t2 else None)
        return node

