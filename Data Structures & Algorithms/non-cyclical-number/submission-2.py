class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited and n != 1:
            visited.add(n)
            total = 0
            for ch in str(n):
                digit = int(ch)
                total += digit ** 2
            n = total
        
        return n == 1