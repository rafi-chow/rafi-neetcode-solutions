from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #1, 2, 30, 4, 50, 3
        #1, 2, 3, 4, 30, 50
        longest = 0
        curr_longest = 0
        if not nums:
            return 0
        for num in num_set:
            #if theres nothing before
            if num - 1 not in num_set:
            #if 1 - 0 (0)
                curr_longest = 0
                first = num
                #1 = num

                #while theres something after:
                while first + 1 in num_set:
                #while 2 in num_set
                    curr_longest += 1
                    #2
                    first += 1
                    #3
            longest = max(curr_longest, longest)
        return longest + 1
                





