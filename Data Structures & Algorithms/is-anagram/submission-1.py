from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #invariant: at the end, both dictionaries should contain the entirety of both strings (first dict with string1, second dict with string2)
        string1 = defaultdict(int)
        string2 = defaultdict(int)
        if len(s) != len(t):
            return False

        for letter in s:
            string1[letter] += 1
        for letter in t:
            string2[letter] += 1

        for letter in s:
            if string1[letter] != string2[letter]:
                return False
        return True