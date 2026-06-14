class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1 and n not in cache:
            cache.add(n)
            n = self.step(n)
        
        return n == 1
        

    def step(self, n: int) -> int:
        res = 0
        for ch in str(n):
            digit = int(ch)
            res += digit ** 2
        return res
