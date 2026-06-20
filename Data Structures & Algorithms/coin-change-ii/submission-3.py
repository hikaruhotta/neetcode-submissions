class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = sorted(coins)
        self.cache = {}
        return self.helper(amount, 0)

    def helper(self, amount: int, index: 0) -> int:
        if amount == 0:
            return 1

        if (amount, index) in self.cache:
            return self.cache[(amount, index)]
        
        result = 0
        for i in range(index, len(self.coins)):
            coin = self.coins[i]
            if coin <= amount:
                result += self.helper(amount - coin, i)

        self.cache[(amount, index)] = result
        
        return result
            