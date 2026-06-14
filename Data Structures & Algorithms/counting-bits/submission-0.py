class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            res = 0
            while i:
                i = i & (i - 1)
                res += 1
            result.append(res)
        return result
            
