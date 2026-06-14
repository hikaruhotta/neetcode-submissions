from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = None

        target = Counter(t)
        window = Counter()

        L = 0
        for R in range(len(s)):
            window[s[R]] += 1

            if not self.isSubset(target, window):
                continue
            
            while self.isSubset(target, window) and L <= R:
                if result is None or len(result) > R - L + 1:
                    result = s[L : R + 1]
                window[s[L]] -= 1
                L += 1

        if result is None:
            result = ""
        
        return result



    def isSubset(self, c1: Counter, c2: Counter) -> bool:
        # determines is c1 is a subset of c2
        for key, freq in c1.items():
            if c2[key] < freq:
                return False
        
        return True
