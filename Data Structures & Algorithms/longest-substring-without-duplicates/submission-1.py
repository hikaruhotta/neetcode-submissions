from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in cnt:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            
            cnt[s[right]] += 1
            result = max(result, right - left + 1)
        
        return result



    

            


            
            