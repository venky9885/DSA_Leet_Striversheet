# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# easiest
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ls = []
        self.ct = 0

        def inr(root):
            if(not root):
                return
            inr(root.left)
            self.ls.append(root.val)
            inr(root.right)
        inr(root)

    def next(self) -> int:
        self.ct += 1

        return self.ls[self.ct-1]

    def hasNext(self) -> bool:
        if(self.ct < len(self.ls)):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
