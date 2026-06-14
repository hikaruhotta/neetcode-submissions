class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cache = {0: 1}
        
        curr_prefix_sum = 0
        for i, num in enumerate(nums):
            curr_prefix_sum += num
            if curr_prefix_sum - k in cache:
                res += cache[curr_prefix_sum - k]
            if curr_prefix_sum not in cache:
                cache[curr_prefix_sum] = 0
            cache[curr_prefix_sum] += 1
        
        return res
