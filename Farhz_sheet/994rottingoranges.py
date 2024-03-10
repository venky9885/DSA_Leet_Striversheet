# it is important problem in BFS'
# BFS means going bready=th first by using queue DS


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # problem related to BFS
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        # get all rotten ornages indexes and fresh orange count
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2):
                    q.append((i, j))
                elif(grid[i][j] == 1):
                    fresh += 1
        # print(fresh,q)
        bound = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # until q or fresh becomes 0 run it
        while(q and fresh > 0):
            # we have to do simulataneously so  loop all q (here q size will change but take the length which is old)
            for i in range(len(q)):
                x, y = q.popleft()
                # take 1 and run all directions in row i
                for dx, dy in bound:
                    nx, ny = dx+x, dy+y
                    # if it is not equal to 1 continue
                    if(nx < 0 or nx == rows or ny < 0 or ny == cols or grid[nx][ny] != 1):
                        continue
                    # if it is 1 rott it
                    grid[nx][ny] = 2
                    # append the coordinate and decrement the fresh
                    q.append((nx, ny))
                    fresh -= 1
            # after a simulataneous  run of 1 complete q then increment timer
            time += 1
        # print(fresh,time)
        return time if(fresh == 0) else -1
