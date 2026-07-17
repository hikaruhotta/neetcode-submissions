class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # "ZZ" = 26*(26^1) + 26*(26^0) = 702
        # "AAA" = 1*(26^2) + 1*(26^1) + 1*(26^0) = 703
        
        result = []
        n = 31
        while columnNumber > 0:
            if self.allAValue(n) <= columnNumber:
                div = columnNumber // 26 ** n
                columnNumber -= div * (26 ** n)
                result.append(div)
            n -= 1
        print(result)
        
        return "".join([chr(ord('A') + num - 1) for num in result])
    
    def allAValue(self, n: int) -> int:
        res = 0
        for i in range(n + 1):
            res += 26 ** i
        return res
