class MinStack:

    def __init__(self):
        self.stack = []
        self.newStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.newStack or val <= self.newStack[-1]:
            self.newStack.append(val)

    def pop(self) -> None:
        if self.newStack and self.stack[-1] == self.newStack[-1]:
            self.newStack.pop()
        self.stack.pop()



    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.newStack:
            return self.newStack[-1]
        else:
            return 0
        
