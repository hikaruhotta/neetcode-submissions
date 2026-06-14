class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = set(coins)
        self.cache = {}

        return self.dfs(amount, 0)
    
    def dfs(self, target: int, max_coin: int) -> int:
        if target == 0:
            return 1

        if (target, max_coin) in self.cache:
            return self.cache[(target, max_coin)]
        
        candidates = []
        
        for coin in self.coins:
            if coin >= max_coin and coin <= target:
                candidates.append(self.dfs(target - coin, coin))

        self.cache[(target, max_coin)] = sum(candidates)
        
        return sum(candidates)
