from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        res = []

        i = 0

        while i < len(s):
            start_i = i
            substr_ch = set([s[i]])
            count[s[i]] -= 1
            i += 1

            while i < len(s) and not self.isSubStrEnd(substr_ch, count):
                substr_ch.add(s[i])
                count[s[i]] -= 1
                i += 1
            
            res.append(i - start_i)
        
        return res

    
    def isSubStrEnd(self, substr_ch, count) -> bool:
        for ch in substr_ch:
            if count[ch] != 0:
                return False
        
        return True

        