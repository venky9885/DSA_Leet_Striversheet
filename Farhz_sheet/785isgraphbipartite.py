class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # here bipartite means neighbour nodes should not be in same set after partition in to 2 sets
        # so we divide odd and even set for odd = 1 even = -1 normally = 0
        odd = [0]*len(graph)

        def bfs(i):
            if(odd[i]):
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                # print(i,q)
                i = q.popleft()
                for nei in graph[i]:
                    if(odd[i] == odd[nei]):
                        return False
                    elif(not odd[nei]):
                        q.append(nei)
                        odd[nei] = -1*odd[i]
            return True
            # for ex [[1,2,3],[0,2],[0,1,3],[0,2]]
            # [1,2,3]in odd and [0 ] in even
            # on second loop it will be in same odd side so we return
        for i in range(len(graph)):
            # if its already there means it returns true then continue
            t = bfs(i)
            print(t)
            if(not t):
                return False
        return True
