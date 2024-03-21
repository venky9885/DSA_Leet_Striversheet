"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        que = deque([root])
        # we do bfs
        while que and que[0]:
            length = len(que)
            for i in range(length):
                curr = que.popleft()
                # we skip at root level and intially assign none because single node like [1]
                # from next step we will have full list values like [2,3]
                # we pop from left side so que[0] and assign next poinetr until lenght less than that
                curr.next = que[0] if i+1 < length else None
                if(curr.left):
                    que.append(curr.left)
                if(curr.right):
                    que.append(curr.right)
        return root
