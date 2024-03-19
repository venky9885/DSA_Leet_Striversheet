# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# for refernce watch https://www.youtube.com/watch?v=2IHdqU48N2w
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        # we create all nodes like parents and 2 child in this graph
        graph = defaultdict(list)

        q = collections.deque([root])

        while q:
            node = q.popleft()
            if(node.left):
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if(node.right):
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        # we add to visit after completion
        res = []
        # we directly start from target node
        que = collections.deque([(target, 0)])
        vis = set([target])
        # we travel to every edge from that node
        while que:
            node, ind = que.popleft()
            # index equals add to array
            if(ind == k):
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in vis:
                        vis.add(edge)
                        que.append((edge, ind+1))

        return res
