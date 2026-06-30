class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num, freq = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] != majority_num:
                freq -= 1
                if freq == 0:
                    majority_num = nums[i]
                    freq = 1
            else:
                freq += 1
        return majority_num