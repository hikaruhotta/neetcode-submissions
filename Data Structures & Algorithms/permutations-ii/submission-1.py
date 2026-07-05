from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        cnt = Counter(nums)
        self.result = []
        self.helper([], cnt)
        return self.result
    
    def helper(self, path: List[int], cnt: Counter) -> None:
        if len(path) == len(self.nums):
            self.result.append(path.copy())
            return
        
        for num, freq in cnt.copy().items():
            path.append(num)
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]
            self.helper(path, cnt)
            cnt[num] += 1
            path.pop()
                



        

