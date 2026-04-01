class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == "}":
                if stack and stack[-1] != "{":
                    return False
                elif not stack:
                    return False
                else:
                    if stack:
                        stack.pop()
            elif char == ")":
                if stack and stack[-1] != "(":
                    return False
                elif not stack:
                    return False
                else:
                    if stack:
                        stack.pop()
            elif char == "]":
                if stack and stack[-1] != "[":
                    return False
                elif not stack:
                    return False
                else:
                    if stack:
                        stack.pop()

        if stack:
            return False
        return True
