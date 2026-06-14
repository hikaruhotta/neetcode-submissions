class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sums.append(0)
            else:
                prefix_sums.append(prefix_sums[-1] + nums[i - 1])
        
        suffix_sums = []
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                suffix_sums.append(0)
            else:
                suffix_sums.append(suffix_sums[-1] + nums[i + 1])
        suffix_sums = suffix_sums[::-1]
        
        for i in range(len(prefix_sums)):
            if prefix_sums[i] == suffix_sums[i]:
                return i
        
        return -1
