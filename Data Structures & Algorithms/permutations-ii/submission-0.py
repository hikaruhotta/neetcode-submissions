from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        cnt = Counter(nums)
        self.results = []

        self.helper(cnt, [])
        return self.results
    
    def helper(self, cnt: Counter, curr: List[int]):
        if len(cnt) == 0:
            self.results.append(curr.copy())
            return
        
        cnt_tmp = cnt.copy()
        for key, freq in cnt_tmp.items():
            cnt[key] -= 1
            if cnt[key] == 0:
                del cnt[key]
            self.helper(cnt, curr + [key])
            cnt[key] += 1
