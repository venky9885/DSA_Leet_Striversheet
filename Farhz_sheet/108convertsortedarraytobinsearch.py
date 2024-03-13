# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#watch neetcode https://www.youtube.com/watch?v=0K0uCMYq5ng&ab_channel=NeetCode
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def hp(l,r):
            if( l > r):
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = hp(l,m-1)
            root.right = hp(m+1,r)
            return root
        return hp(0,len(nums)-1)
        

        
