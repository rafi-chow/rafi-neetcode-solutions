class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack


    def push(self, val: int) -> None:
        self.val = val
        self.stack.append(self.val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return (self.stack[-1])

    def getMin(self) -> int:
        return min(self.stack)
        
