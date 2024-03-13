# wtach neetcode https://www.youtube.com/watch?v=nONCGxWoUfM

from typing import List


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


# or


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # Sort intervals based on end time

        count = 1  # At least one interval will be non-overlapping
        end_time = intervals[0][1]  # End time of the first interval

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                count += 1
                end_time = intervals[i][1]

        # Count of overlapping intervals will be total intervals - non-overlapping intervals
        return len(intervals) - count
