class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        static = 0
        sort = sorted(nums)
        output = []

        while static < len(nums) - 2:
            while static < len(nums) - 2 and static > 0 and sort[static] == sort[static - 1]:
                static += 1
                continue
            L = static + 1
            R = len(nums) - 1
            while L < R:
                total = sort[static] + sort[L] + sort[R]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                elif total == 0:
                    output.append((sort[static], sort[L], sort[R]))
                    L += 1
                    R -= 1
                    while L < R and sort[L] == sort[L - 1]:
                        L += 1
                    while L < R and sort[R] == sort[R + 1]:
                        R -= 1
            static += 1
        return output
