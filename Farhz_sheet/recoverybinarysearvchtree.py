# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=bJBwOMPhe6Y Explained very easily by timothy
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.temp = []

        def dfs(node):
            if(not node):
                return
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)
        dfs(root)
        # because for bst eveything in sorted order so
        # we take every node in temp array
        # then for each node we replace val with new sorted val
        # in directly nodes in place
        s = (sorted(i.val for i in self.temp))
        for i in range(len(self.temp)):
            self.temp[i].val = s[i]

        """
        Do not return anything, modify root in-place instead.
        """


# anothe solution form submissions
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if self.pre and not self.first and self.pre.val > node.val:
                self.first = self.pre
            if self.first and self.pre.val > node.val:
                self.second = node
            self.pre = node
            traverse(node.right)

        self.first = None
        self.second = None
        self.pre = None
        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
