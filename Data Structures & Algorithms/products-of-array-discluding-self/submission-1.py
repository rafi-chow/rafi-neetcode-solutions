class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left, right
        output = [1] * len(nums)
        left_mult = 1
        for i in range(len(nums)):
            output[i] *= left_mult
            left_mult *= nums[i]
        right_mult = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_mult
            right_mult *= nums[i]
        return output
