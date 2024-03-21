# https://www.youtube.com/watch?v=Uei1fwDoyKk

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1/values[i]])

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in graph[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)

            # if path doesnt connect
            return -1
        return [bfs(i[0], i[1]) for i in queries]
