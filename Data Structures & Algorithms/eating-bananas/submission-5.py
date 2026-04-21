import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        output = 0
        while L <= R:
            mid = (L + R) // 2 #1 + 4 5 // 2 = 2
            speed = 0
            for pile in piles:
                speed += math.ceil(pile / mid) #1 / 2 = 1. 4/2 = 2. 3/2 = 2. 2/2 = 1. 1, 3, 4, 6.
            if speed <= h:
                output = mid
                R = mid - 1
            else:
                L = mid + 1
        return output