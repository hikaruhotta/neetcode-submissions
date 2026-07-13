class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        num = 1
        while num*num <= n:
            nums.append(num*num)
            num += 1
        nums = sorted(nums, reverse=True)

        self.cache = {}
        return self.helper(n, nums)
    
    def helper(self, n: int, nums: List[int]) -> int:
        if n == 0:
            return 0
        
        if n in self.cache:
            return self.cache[n]
        
        candidates = []
        for num in nums:
            if num <= n:
                candidates.append(1 + self.helper(n - num, nums))
        result = min(candidates)
        self.cache[n] = result
        return result
