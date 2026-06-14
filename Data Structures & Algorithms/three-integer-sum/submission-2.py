class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums = sorted(nums)
        print(nums)

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            two_sum_results = self.twoSum(nums[i + 1:].copy(), target)
            for two_sum_result in two_sum_results:
                results.append([nums[i], two_sum_result[0], two_sum_result[1]])
        
        return results
            
        
    def twoSum(self, nums: List[int], target: int):
        result = []

        L, R = 0, len(nums) - 1

        while L < R:
            if nums[L] + nums[R] == target:
                result.append([nums[L], nums[R]])
                L += 1
                R -=1
                while nums[L] == nums[L - 1] and L < R:
                    L += 1

            elif nums[L] + nums[R] > target:
                R -= 1
            else:
                L += 1
        return result