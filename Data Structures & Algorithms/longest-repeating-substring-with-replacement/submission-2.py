from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window is counter but you need to keep track of most frequent char and frequency
        # an acceptable window is window size - max_freq <= k
        result = 0

        window = Counter()
        max_f = 0

        L = 0

        for R in range(len(s)):
            window[s[R]] += 1
            max_f = max(max_f, window[s[R]])
                
            while (R - L + 1) - max_f > k and L < R:
                window[s[L]] -= 1
                if window[s[L]] == 0:
                    del window[s[L]]
                L += 1
            
            result = max(result, R - L + 1)
        
        return result
