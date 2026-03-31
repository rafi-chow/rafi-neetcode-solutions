class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #probably keep track of distance
        #49 x 5 = 250
        #42 x 7
        L = 0
        R = len(heights) - 1
        biggest_sum = 0
        while L < R:
            distance = R - L
            curr_sum = min(heights[L],heights[R]) * distance
            if curr_sum > biggest_sum:
                biggest_sum = curr_sum
                if heights[L] < heights[R]:
                    L += 1
                elif heights[R] < heights[L]:
                    R -= 1
            elif heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
            elif heights[R] == heights[L]:
                L += 1
        return biggest_sum
