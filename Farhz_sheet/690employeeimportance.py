"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        q = deque([id])
        sm = 0
        while q:
            p = q.popleft()
            for i in employees:
                if(i.id == p):
                    sm+=i.importance
                    q.extend(i.subordinates)
                    break
        return sm
        
