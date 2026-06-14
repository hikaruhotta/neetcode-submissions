from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_cnt = Counter(s1)
        window = Counter()
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            
            while (window & s1_cnt) == s1_cnt and left <= right:
                if window == s1_cnt:
                    return True

                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left += 1
                
        return False


            
                


        