class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        result = x
        while L <= R:
            M = L + (R - L) // 2
            squared = M * M
            if squared <= x:
                result = M
                L = M + 1
            else:
                R = M - 1
        return result