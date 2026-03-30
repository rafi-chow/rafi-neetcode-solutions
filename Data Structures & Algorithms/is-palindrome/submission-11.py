class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        low = str(s.lower())
        while L < R:
            if low[L].isalnum() == False:
                L += 1
            elif low[R].isalnum() == False:
                R -= 1
            elif low[L] == low[R]:
                L += 1
                R -= 1
            else:
                return False
        return True
