from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            current_sum = numbers[L] + numbers[R]
            if current_sum > target:
                R -= 1
            if current_sum < target:
                L += 1
            if current_sum == target:
                return list((L + 1, R + 1))
