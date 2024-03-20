# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        width = 0
        while q:
            _, left = q[0]
            _, right = q[-1]
            width = max(width, right-left+1)
            nextLevel = deque()
            while q:
                node, index = q.popleft()
                # for left tree index * 2
                if(node.left):
                    nextLevel.append((node.left, index*2))
                # for right tree index * 2 +1(+1 is root node)
                if(node.right):
                    nextLevel.append((node.right, index*2+1))
            q = nextLevel
        return width
