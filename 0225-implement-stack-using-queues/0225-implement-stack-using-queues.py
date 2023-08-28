class MyStack:

    def __init__(self):
        self.Array = []
        

    def push(self, x: int) -> None:
        self.Array.append(x)
        

    def pop(self) -> int:
        last = self.Array[-1]
        self.Array = self.Array[:len(self.Array) -1]
        return last
        

    def top(self) -> int:
        return self.Array[-1]

    def empty(self) -> bool:
        return self.Array == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()