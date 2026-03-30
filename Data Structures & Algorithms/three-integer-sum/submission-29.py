class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        output = []
        static = 0
        #-4, -1, -1, 0, 1, 2

        while static < len(nums) - 2:
            while static > 0 and static < len(new) - 2 and new[static] == new[static - 1]:
                static += 1
                continue
            L = static + 1
            R = len(nums) - 1

            while L < R:
                current_sum = new[L] + new[R] + new[static]
                if current_sum > 0:
                    R -= 1
                elif current_sum < 0:
                    L += 1
                elif current_sum == 0:
                    output.append((new[L], new[R], new[static]))
                    R -= 1
                    L += 1
                    while L < R and new[L] == new[L - 1]:
                        L += 1
                    while L < R and new[R] == new[R + 1]:
                        R -= 1
            static += 1

        return output
