# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#this is very simple do nor inordertraversal and imp thing is when compoaring prev

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        res = True
        def inorder(node):
            nonlocal prev,res

            if not node: return 
            inorder(node.left)
            # dont use if not prev instaed use is not None for 0 its stops
            if(prev is not None and node.val <= prev):
                print(4272,node.val,prev)
                res =  False
                return 
            prev = node.val
            inorder(node.right)

        inorder(root)    
        return res

        