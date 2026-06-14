from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        if len(hash_set) < 2:
            return len(hash_set)

        candidates = []
        hash_set = set(nums)
        for num in nums:
            if num + 1 in hash_set and num - 1 not in hash_set:
                candidates.append(num)

        result = []
        for candidate in candidates:
            count = 0
            curr = candidate
            while curr in hash_set:
                count += 1
                curr += 1
            result.append(count)
        return max(result)
 
