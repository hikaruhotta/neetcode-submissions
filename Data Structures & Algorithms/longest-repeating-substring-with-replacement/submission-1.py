from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        left = 0
        result = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            while self.numReplacementsNeeded(cnt) > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            result = max(result, right - left + 1)

        
        return result

    def numReplacementsNeeded(self, cnt):
        if len(cnt) == 0:
            return 0

        max_count = cnt.most_common(1)
        return cnt.total() - max_count[0][1]
