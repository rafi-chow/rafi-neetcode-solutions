class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid


            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                #1, 2, 3, 4, 5
                    R = mid - 1
                else:
                    L = mid + 1

            else:
                if nums[R] >= target > nums[mid]:
                #1, 2, 3, 4, 5
                    L = mid + 1
                else:
                    R = mid - 1
            
        return -1