class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False

        if sum(nums) % k != 0:
            return False

        self.nums = sorted(nums, reverse=True)
        return self.helper(0, [0 for i in range(k)])
    
    def helper(self, index: int, subset_sums: List[int]) -> bool:
        if index == len(self.nums):
            if all([subset_sum == subset_sums[0] for subset_sum in subset_sums]):
                return True
            else:
                return False

        results = []
        prev_sums = set()
        for i in range(len(subset_sums)):
            if subset_sums[i] + self.nums[index] > sum(self.nums) // len(subset_sums):
                continue

            if subset_sums[i] in prev_sums:
                continue

            subset_sums[i] += self.nums[index]
            res = self.helper(index + 1, subset_sums)
            results.append(res)
            subset_sums[i] -= self.nums[index]
            prev_sums.add(subset_sums[i])

        return any(results)


    