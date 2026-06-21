from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        result = []

        L = 0
        while L < len(s):
            R = L
            window = set()
            while R < len(s) and not self.isValidWindow(window, cnt):
                window.add(s[R])
                cnt[s[R]] -= 1
                if cnt[s[R]] == 0:
                    del cnt[s[R]]
                R += 1
        
            result.append(R - L)
            L = R
        return result
        

    def isValidWindow(self, window, cnt) -> bool:
        if len(window) == 0:
            return False
        for ch in window:
            if cnt[ch] > 0:
                return False
        return True