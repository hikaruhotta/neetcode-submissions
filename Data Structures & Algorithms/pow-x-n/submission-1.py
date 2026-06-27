class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.cache = {}
        if n < 0:
            x = 1 / x
            n = -n

        result = self.helper(x, n)
        return result
    
    def helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        if n in self.cache:
            return self.cache[n]

        if n % 2 == 0:
            a, b = n // 2, n // 2
        else:
            a, b = n // 2 + 1, n // 2
        
        result = self.helper(x, a) * self.helper(x, b)
        self.cache[n] = result
        return result