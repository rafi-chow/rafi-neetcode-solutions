from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #1, 2, 30, 4, 50, 3
        #1, 2, 3, 4, 30, 50
        longest = 0
        curr_len = 1
        for num in num_set:
            #if theres nothing before
            if num - 1 not in num_set:
                #increase while there is something after
                curr_len = 1
                while num + 1 in num_set:
                    curr_len += 1
                    num = num + 1
            longest = max(curr_len, longest)

        return longest
                





