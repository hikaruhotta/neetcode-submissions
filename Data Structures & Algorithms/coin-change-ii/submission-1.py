class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins[::-1]
        self.cache = {}

        return self.dfs(amount, 0)
    
    def dfs(self, target: int, index: int) -> int:
        if target == 0:
            return 1
        elif index >= len(self.coins):
            return 0

        if (target, index) in self.cache:
            return self.cache[(target, index)]
            
        total = 0
        for num in range(target // self.coins[index] + 1):
            total += self.dfs(target - self.coins[index] * num, index + 1)
        
        self.cache[(target, index)] = total
        
        return total

