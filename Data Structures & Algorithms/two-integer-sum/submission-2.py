class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in nums_index:
                complement_index = nums_index[target - num]
                if complement_index != i:
                    return [i, complement_index]