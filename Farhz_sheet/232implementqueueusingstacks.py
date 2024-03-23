class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, x: int) -> None:
        self.stk1.append(x)

        

    def pop(self) -> int:
        while(self.stk1 and len(self.stk1) != 1):
            self.stk2.append(self.stk1.pop())
        # self.stk1 = [x]
        while(self.stk2):
            self.stk1.append(self.stk2.pop())

        return self.stk1.pop(0)
        

    def peek(self) -> int:
        return self.stk1[0]
        

    def empty(self) -> bool:
        return len(self.stk1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()