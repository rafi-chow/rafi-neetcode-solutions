class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        if len(s) == 0:
            return True


        new = []
        for char in s.lower():
            if char == " ":
                continue
            elif char.isalnum() == False:
                continue
            new.append(char)
        
        print(new)
        R = len(new) - 1
        if len(new) <= 1:
            return True

        while L < R:
            if new[L] != new[R]:
                return False
            else:
                L += 1
                R -=1
        return True
