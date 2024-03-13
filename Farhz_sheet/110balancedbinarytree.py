
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(root):
            if(not root):return [True,0]#first go to depth of binary tree and return [True,0]
            left,right=f(root.left),f(root.right)
            #check the balance for every sub tree and return upside
            balance = left[0] and right [0] and abs(left[1] - right[1]) <= 1
            return [balance,1+max(left[1] ,right[1])]
        return f(root)[0]

