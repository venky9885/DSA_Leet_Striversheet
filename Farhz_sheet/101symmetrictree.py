# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://www.youtube.com/watch?v=Mao9uzxwvmc&ab_channel=NeetCodeIO
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(left,right):
            #both nodes are null return True
            if(not left and not right):
                return True
            #if  either one node is present return false
            if(not left or not right):
                return False
            #here we are comparing left tree left most node and rightree right most node and inner nodees f(left.right ,right.left)
            return left.val==right.val  and f(left.left,right.right) and f(left.right ,right.left)
            


        # print(f(root))
        return f(root.left,root.right)
            
            

        
