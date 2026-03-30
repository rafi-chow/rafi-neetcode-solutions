from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #the hashmap must contain every number already seen, mapped to its frequency
        seen = defaultdict(int)
        output = []
        for num in nums:
            seen[num] += 1
            #1: 1
            #2: 2
            #3: 3
            #want: top k (2, 3)
        while k > 0:
            max_key = max(seen, key = seen.get)

            output.append(max_key)
            del seen[max_key]
            k -= 1
        return output
