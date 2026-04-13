class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            #1 2 3 4 5 6 8
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
        return -1

            



        