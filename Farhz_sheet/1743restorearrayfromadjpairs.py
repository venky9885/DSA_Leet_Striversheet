class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # draw points then you will get acyclic grap
        # create graph,tip is adjacent pairs
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        res = []
        # we will have either single or 2 neighbours like [1] or [1,2]
        # we need a node with single neighbour
        for node, neigbours in graph.items():
            if(len(neigbours) == 1):
                res = [node, neigbours[0]]
                break

        # from that point start itreating through grap
        while len(res) < len(adjacentPairs) + 1:
            last, prev = res[-1], res[-2]
            candi = graph[last]
            # if it is equal  take another or continue to append
            nextEl = candi[0] if candi[0] != prev else candi[1]
            res.append(nextEl)
        # return element
        return res
