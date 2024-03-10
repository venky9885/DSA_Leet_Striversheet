# wtach neetcode https://www.youtube.com/watch?v=nONCGxWoUfM

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # they are not overlapping
            if(start >= prevEnd):
                prevEnd = end
            # here overlapping
            else:
                res += 1
                # so at ind 1 for arr =  [[1,3],[2,4]] = > min(3,4) => prevEnd = 3
                prevEnd = min(prevEnd, end)
                print(prevEnd)
        return res
