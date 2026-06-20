class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [1, 1]
        for i in range(1, len(s)):
            res = 0
            if s[i - 1] != '0':
                two_digit = int(s[i - 1 : i + 1])
                if two_digit <= 26:
                    res += dp[-2]
            
            if s[i] != '0':
                res += dp[-1]
            dp.append(res)

        return dp[-1]

# [1, 1 2 3]