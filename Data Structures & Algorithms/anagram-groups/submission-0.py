from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #what must be true?:
            #all the words ive seen ust be grouped with their matching anagram
        output = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            output[key].append(string)
        return list(output.values())
