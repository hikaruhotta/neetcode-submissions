import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            if not self.canConsume(piles, h, mid):
                left = mid + 1
            else:
                prev_can_consume = self.canConsume(piles, h, mid - 1)
                if prev_can_consume:
                    right = mid - 1
                else:
                    return mid
            
    def canConsume(self, piles, h, eating_rate):
        if eating_rate == 0:
            return False
        total_time = 0
        for pile in piles:
            total_time += math.ceil(float(pile) / eating_rate)
        return total_time <= h


            
