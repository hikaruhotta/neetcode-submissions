from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)

        window = Counter()

        L = 0

        for i in range(len(s2) - len(s1) + 1):
            if len(window) == 0:
                window = Counter(s2[i : i + len(s1)])
            else:
                window[s2[i - 1]] -= 1
                if window[s2[i - 1]] == 0:
                    del window[s2[i - 1]]

                window[s2[i + len(s1) - 1]] += 1
            
            if window == target:
                return True
            
        return False
