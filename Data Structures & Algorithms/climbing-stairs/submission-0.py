class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for _ in range(n)]
        
        for i in range(n):
            if i == 0:
                cache[i] = 1
            elif i == 1:
                cache[i] = 2
            else:
                cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[-1]
