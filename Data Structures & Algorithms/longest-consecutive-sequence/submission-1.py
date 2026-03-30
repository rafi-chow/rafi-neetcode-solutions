from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #(1,2,3)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
            #if 0 - 1 (-1) not in num_set:
            #if 1 not in num(set)
                length = 1

                while num + length in num_set:
                #while 0 + 1, 2, 3 in num_set
                    length += 1
                
                longest = max(longest, length)
        return longest


