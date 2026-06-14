class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.x = x
        self.cache = {}
        if n >= 0:
            return self.helper(n)
        else:
            return 1 / self.helper(abs(n))

    def helper(self, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return self.x

        if n in self.cache:
            return self.cache[n]

        if n % 2 == 0:
            return self.helper(n // 2) * self.helper(n // 2)
        else:
            return self.helper(((n - 1) // 2) + 1) * self.helper((n - 1) // 2)
        
        
        