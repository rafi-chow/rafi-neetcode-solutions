class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        #-4, -1, -1, 0, 1, 2
        first = 0
        output = []
        while first < len(nums) - 1:
            L = first + 1
            R = len(nums) - 1
            while L < R:
                current_sum = new[L] + new[R] + new[first]
                if current_sum > 0:
                    R -= 1
                elif current_sum < 0:
                    L += 1
                elif current_sum == 0:
                    output.append((new[L], new[R], new[first]))
                    L += 1
                    R -= 1
            first += 1

        return list(set(output))