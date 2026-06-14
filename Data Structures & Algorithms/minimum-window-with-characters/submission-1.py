from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_cnt = Counter(t)

        left = 0
        window = Counter()
        result = None

        for right in range(len(s)):
            window[s[right]] += 1
            # check that window contains t
            while (t_cnt & window) == t_cnt and left <= right:
                if result is None or len(result) > right - left + 1:
                    result = s[left: right + 1]
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
        
        return result or ""
            

            


