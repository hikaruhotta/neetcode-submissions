class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.cache = {}
        res = self.helper(piles, 0, len(piles) - 1, True)
        return res >= 0
        

    def helper(self, piles: List[int], i: int, j: int, is_alice: bool) -> int:
        if i == j:
            return 0
        
        if (i, j, is_alice) in self.cache:
            return self.cache[(i, j, is_alice)]
        
        # take front
        front = self.helper(piles, i + 1, j, not is_alice)
        if is_alice:
            front += piles[i]
        else:
            front -= piles[i]
        
        # take back
        back = self.helper(piles, i, j - 1, not is_alice)
        if is_alice:
            back += piles[j]
        else:
            back -= piles[j]
        
        if is_alice:
            result = max(front, back)
        else:
            result = min(front, back)

        self.cache[(i, j, is_alice)] = result
        return result
