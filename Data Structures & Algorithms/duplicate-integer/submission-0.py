from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] += 1
        return False