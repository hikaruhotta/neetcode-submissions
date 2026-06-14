import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = sorted(piles)
        low, high = 1, self.piles[-1] * len(self.piles)

        if self.canEat(h, 1):
            return 1

        while low <= high:
            mid = low + (high - low) // 2
            prev_can_eat = self.canEat(h, mid - 1)
            can_eat = self.canEat(h, mid)
            
            if can_eat and not prev_can_eat:
                return mid
            elif can_eat:
                high = mid - 1
            else:
                low = mid + 1

    def canEat(self, h: int, k: int) -> bool:
        total = 0
        for pile in self.piles:
            total += pile // k
            if pile % k > 0:
                total += 1
            if total > h:
                return False

        return total <= h


            
