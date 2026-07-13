class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.cache = {}
        delta = self.helper(piles, 0, 1, True)
        smaller = (sum(piles) - abs(delta)) // 2
        if delta < 0:
            return smaller
        else:
            return smaller + delta
    
    def helper(self, piles: List[int], index: int, M: int, is_alice: bool) -> int:
        if index == len(piles):
            return 0

        if (index, M, is_alice) in self.cache:
            return self.cache[(index, M, is_alice)]
        
        deltas = []
        for X in range(1, 2 * M + 1):
            if index + X <= len(piles):
                next_M = max(M, X)
                delta = self.helper(piles, index + X, next_M, not is_alice)
                if is_alice:
                    delta += sum(piles[index : index + X])
                else:
                    delta -= sum(piles[index : index + X])
                deltas.append(delta)
        
        if is_alice:
            result = max(deltas)
        else:
            result = min(deltas)

        self.cache[(index, M, is_alice)] = result
        
        return result
                