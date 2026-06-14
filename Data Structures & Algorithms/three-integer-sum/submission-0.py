class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) - 2):
            two_sum_results = self.twoSum(nums[i + 1:], 0 - nums[i])
            for two_sum_result in two_sum_results:
                result.append(tuple(sorted([nums[i]] + two_sum_result)))
        return list(set(result))

    def twoSum(self, nums: List[int], target):
        result = []
        cache = set()
        for num in nums:
            if target - num in cache:
                result.append(sorted([num, target - num]))
            cache.add(num)
        return result

            


