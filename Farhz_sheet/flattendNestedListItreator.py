# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.c = 0
        self.stk = []
        def flt(nesL):
            for i in nesL:
                if(i.isInteger()):
                    self.stk.append(i.getInteger())
                else:
                    flt(i.getList())
        flt(nestedList)
        print(self.stk)

        
    
    def next(self) -> int:
        return self.stk.pop(0)
        
    
    def hasNext(self) -> bool:
        if(self.stk):
            return True
        return False
                 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())