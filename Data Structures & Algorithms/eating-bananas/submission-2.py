class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        L = 1
        R = max(piles)
        output = R
        while L <= R:
            k = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            if hours <= h:
                output = k
                R = k - 1
            if hours > h:
                L = k + 1
        return output

            