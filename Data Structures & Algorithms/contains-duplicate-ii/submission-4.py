class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for delta in range(1, k + 1):
            for i in range(len(nums) - delta):
                j = i + delta
                if nums[i] == nums[j]:
                    return True
        return False

