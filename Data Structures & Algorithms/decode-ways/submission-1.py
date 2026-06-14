class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]

        if s[0] == '0':
            return 0
        else:
            dp.append(1)

        for i in range(1, len(s)):
            total = 0

            if s[i] != '0':
                total += dp[-1]
            
            if i >= 1 and self.isValidGroup(s[i - 1:i + 1]):
                total += dp[-2]
            
            dp.append(total)

        return dp[-1]

    def isValidGroup(self, s: str) -> bool:
        if len(s) == 0 or len(s) > 2:
            return False

        if s[0] == '0':
            return False
        
        return int(s) > 0 and int(s) < 27

            


            


            