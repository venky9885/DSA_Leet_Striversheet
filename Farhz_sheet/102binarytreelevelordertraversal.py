# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# too easy level order traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return
        q = [root]
        ans = []
        while q:
            tp = q
            q = []
            lv = []
            for i in tp:

                if(i.left):
                    q.append(i.left)
                if(i.right):
                    q.append(i.right)
                print(i.val)
                lv.append(i.val)

            ans.append(lv)
        print(ans)
        return ans
