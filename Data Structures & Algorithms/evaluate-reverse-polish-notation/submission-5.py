class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            elif token == "+":
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
            elif token == "-":

                if len(stack) >= 2:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a - b)
            elif token == "*":

                if len(stack) >= 2:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a * b)
            elif token == "/":
                if len(stack) >= 2:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a / b))
        return stack[-1]
