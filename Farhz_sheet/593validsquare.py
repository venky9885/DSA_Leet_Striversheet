class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def l(ar1,ar2):
            return ((ar2[1]- ar1[1])**2+(ar2[0]- ar1[0])**2)
        #it is simple just calulate distance between every 2 possible points
        #then sort them you will get first 4 equal sides and 2 eq diagonlas
        cd = [l(p1,p2),l(p2,p3),l(p3,p4),l(p4,p1),l(p2,p4),l(p1,p3)]
        cd.sort()
        return True if (cd[0] > 0 and cd[0] == cd[1] == cd[2] == cd[3] and (cd[4] == cd[5])) else False
        