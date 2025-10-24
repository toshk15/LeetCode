from collections import deque
class MyStack:

    def __init__(self):
        self.q1=deque()        

    def push(self, x: int) -> None:
        self.q1.append(x)        

    def pop(self) -> int:
        return self.q1.pop()       

    def top(self) -> int:
        return self.q1[-1]       

    def empty(self) -> bool:
        if not self.q1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()