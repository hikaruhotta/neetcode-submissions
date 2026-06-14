class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = None

        while L <= R:
            M = L + (R - L) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / M)
            
            if hours <= h:
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res
