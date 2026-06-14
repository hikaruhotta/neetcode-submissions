class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        
        result = 0
        visited = set()

        for num in nums:
            if num in visited:
                continue
            result_len = 1
            curr_num = num
            while curr_num + 1 in hash_set:
                visited.add(curr_num + 1)
                result_len += 1
                curr_num += 1
            result = max(result, result_len)

        return result
        

