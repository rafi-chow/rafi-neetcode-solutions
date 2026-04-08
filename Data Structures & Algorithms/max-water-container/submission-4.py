class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #probably keep track of distance
        #49 x 5 = 250
        #42 x 7
        L = 0
        R = len(heights) - 1
        total_sum = 0

        while L < R:
            distance = R - L
            curr_sum = min(heights[L], heights[R]) * distance
            if curr_sum >= total_sum:
                total_sum = curr_sum
                if heights[L] > heights[R]:
                    R -= 1
                elif heights[R] > heights[L]:
                    L += 1
                elif heights[R] == heights[L]:
                    L += 1
            elif curr_sum < total_sum:
                if heights[L] > heights[R]:
                    R -= 1
                elif heights[R] > heights[L]:
                    L += 1
                elif heights[R] == heights[L]:
                    L += 1
        return total_sum

