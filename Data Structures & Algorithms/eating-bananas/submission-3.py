import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        L = 1
        R = max(piles)
        output = 0
        while L <= R:
            k = (L + R) // 2 #5 // 2 = 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) #1 // 2 = 1. 4/2 = 2, 3/2 = 2, 2/2 = 1 (6)
            if hours > h:
                #1, 2, 3, 4
                L = k + 1
            elif hours <= h:
                output = k
                R = k - 1
        return output