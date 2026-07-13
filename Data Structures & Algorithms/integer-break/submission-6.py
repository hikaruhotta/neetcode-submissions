class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        self.cache = {}
        results = []
        for i in range(1, n // 2 + 1):
            results.append(self.helper(i) * self.helper(n - i))
        return max(results)

    def helper(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        candidates = [n]
        for i in range(1, n // 2 + 1):
            candidates.append(self.helper(i) * self.helper(n - i))
        
        result = max(candidates)
        self.cache[n] = result
        return result