from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #the hashmap must contain every number already seen, mapped to its frequency
        if k == 0:
            return 0

        output = []
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        #find max value in seen, add its key to output, remove that from dict

        for i in range(k):
            max_key = max(seen, key = seen.get)

            output.append(max_key)

            del seen[max_key]

        return output

