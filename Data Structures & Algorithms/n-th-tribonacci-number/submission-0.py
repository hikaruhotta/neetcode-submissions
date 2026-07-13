class Solution:
    def tribonacci(self, n: int) -> int:
        self.cache = {}
        return self.helper(n)
    
    def helper(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        if n in self.cache:
            return self.cache[n]
        
        result = self.helper(n - 3) + self.helper(n - 2) + self.helper(n - 1)
        self.cache[n] = result
        return result