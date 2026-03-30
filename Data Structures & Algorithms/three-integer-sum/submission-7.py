class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        first = 0
        output = []
        #4, -1, -1, 2, -4

        while first < len(nums) - 2:
            if first > 0 and new[first] == new[first - 1]:
                first += 1
                continue
            L = first + 1
            R = len(nums) - 1
            while L < R:
                current_sum = new[L] + new[R] + new[first]
                if current_sum > 0:
                    R -= 1
                elif current_sum < 0:
                    L += 1
                elif current_sum == 0:
                    output.append([new[L], new[R], new[first]])
                    L += 1
                    R -= 1
                    while L < R and new[L] == new[L - 1]:
                        L += 1
                    while L < R and new[R] == new[R + 1]:
                        R -= 1
            first += 1
        return output

        