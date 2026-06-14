from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_cnt = Counter()
        left = 0

        result = 0

        for right in range(len(s)):
            while s[right] in char_cnt:
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    del char_cnt[s[left]]
                left += 1
            char_cnt[s[right]] += 1
            result = max(result, right - left + 1)

        return result


    

            


            
            