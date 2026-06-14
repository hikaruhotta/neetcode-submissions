from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        L = 0
        window = Counter()

        for R in range(len(s)):
            window[s[R]] += 1

            while len(window) < R - L + 1 and L < R:
                window[s[L]] -= 1
                if window[s[L]] == 0:
                    del window[s[L]]
                L += 1
            
            result = max(result, R - L + 1)
        
        return result