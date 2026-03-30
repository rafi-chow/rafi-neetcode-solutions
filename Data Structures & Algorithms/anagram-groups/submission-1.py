from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #what must be true?:
            #all the words ive seen ust be grouped with their matching anagram
        seen = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            seen[key].append(s)
        return (list(seen.values()))
            
