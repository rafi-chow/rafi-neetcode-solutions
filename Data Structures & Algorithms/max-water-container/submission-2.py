class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #probably keep track of distance
        #49 x 5 = 250
        #42 x 7
        L = 0
        R = len(heights) - 1
        curr_max = 0
        while L < R:
            distance = R - L
            curr_sum = min(heights[L], heights[R]) * distance
            curr_max = max(curr_max, curr_sum)

            if heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
            elif heights[R] == heights[L]:
                R -= 1
        return curr_max

