from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)

        window = Counter()

        L = 0

        for R in range(len(s2)):
            window[s2[R]] += 1

            while not self.isSubset(window, target) and L < R:
                window[s2[L]] -= 1
                L += 1
            
            if window == target:
                return True
        
        return False


    def isSubset(self, c1: Counter, c2: Counter) -> bool:
        # computed whether c1 is a subset of c2
        # O(1) because only lowercase letters

        for key, freq in c1.items():
            if c2[key] < freq:
                return False
        
        return True