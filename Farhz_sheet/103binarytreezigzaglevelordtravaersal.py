# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# it is also very simple  here level order
# one level is normal append
# another level is reverse and append
# we do bfs

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        cnt = 0
        while queue:
            temp = queue
            queue = []
            level = []
            for node in temp:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            # ans.append(level)
            cnt += 1

            if cnt % 2 != 0:
                ans.append(level)
            else:
                ans.append(level[::-1])
        print(ans)
        return ans
