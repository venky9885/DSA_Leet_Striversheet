# https://leetcode.com/problems/spiral-matrix/description/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            if(matrix):
                res.extend(matrix.pop(0))
            for rw in matrix:
                if(rw):
                    res.append(rw.pop(-1))
            if(matrix):
                res.extend(matrix.pop(-1)[::-1])
            res.extend(reversed([row.pop(0) for row in matrix if row]))
        return res
        