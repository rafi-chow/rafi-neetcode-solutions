class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}" : "{", "]" : "[", ")" : "("}

        for char in s:
            if char in pairs.values():
                stack.append(char)
                #[
            else:
                if not stack or stack and pairs[char] != stack[-1]:
                    #pairs["["]
                    
                    return False
                elif stack and pairs[char] == stack[-1]:
                    stack.pop()

        if stack:
            return False
        return True