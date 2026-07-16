class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}

        result = 0

        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in prefix_sums:
                result += prefix_sums[curr_sum - k]
            if curr_sum not in prefix_sums:
                prefix_sums[curr_sum] = 0
            prefix_sums[curr_sum] += 1
        
        return result