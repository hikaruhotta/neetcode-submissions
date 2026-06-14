class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        while L <= R:
            M = L + (R - L) // 2
            M_h = self.getHours(piles, M)
            M_prev_h = self.getHours(piles, M - 1)

            if M_h <= h and h < M_prev_h:
                return M
            elif M_h <= h and M_prev_h <= h:
                R = M - 1
            else:
                L = M + 1
        return L
        


    def getHours(self, piles: List[int], r: int) -> float:
        if r == 0:
            return float('inf')

        hours = 0
        for pile in piles:
            if pile % r == 0:
                hours += pile // r
            else:
                hours += pile // r + 1
        return hours