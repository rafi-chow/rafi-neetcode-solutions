class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[R] < nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid
                else:
                    L = mid + 1
            elif nums[R] > nums[mid]:
                # 1, 2, 3, 4, 5, 6
                if nums[R] >= target > nums[mid]:
                    L = mid + 1
                else:
                    R = mid
            else:
                return -1
        return -1
