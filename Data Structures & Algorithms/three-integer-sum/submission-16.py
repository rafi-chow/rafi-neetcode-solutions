class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        output = []
        static = 0
        #-4, -1, -1, 0, 1, 2

        while static < len(nums) - 2:
            L = static + 1
            R = len(nums) - 1
            if static > 0 and new[static] == new[static - 1]:
                static += 1
                continue
            while L < R:
                current_sum = new[L] + new[R] + new[static]
                if current_sum > 0:
                    R -= 1
                elif current_sum < 0:
                    L += 1
                elif current_sum == 0:
                    output.append((new[static], new[L], new[R]))
                    L += 1
                    R -= 1
                    while L < R and new[L] == new[L - 1]:
                        L += 1
                    while L < R and new[R] == new[R + 1]:
                        R -= 1
            static += 1
        return output