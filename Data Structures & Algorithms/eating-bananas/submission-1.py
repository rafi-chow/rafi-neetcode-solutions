class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        #1,2,3,4
        L = 1
        R = max(piles)
        output = R
        while L <= R:
            k = (L + R) // 2
            hours = 0
            #2
            for pile in piles:
                hours += (pile + k - 1) // k
            #5
            if hours <= h:
                output = k
                R = k - 1
            elif hours > h:
                L = k + 1
        return output
