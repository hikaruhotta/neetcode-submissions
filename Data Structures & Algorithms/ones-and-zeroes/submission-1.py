class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []

        for s in strs:
            zeroes, ones = 0, 0
            for ch in s:
                if ch == '0':
                    zeroes += 1
                else:
                    ones += 1
            counts.append((zeroes, ones))
        
        self.cache = {}
        self.counts = counts
        return self.helper(0, m, n)

    def helper(self, index, m, n) -> int:
        if index == len(self.counts):
            return 0

        if (index, m, n) in self.cache:
            return self.cache[(index, m, n)]
        
        skip = self.helper(index + 1, m, n)

        include = 0
        zeroes, ones = self.counts[index]

        if zeroes <= m and ones <= n:
            include = 1 + self.helper(index + 1, m - zeroes, n - ones)

        result = max(skip, include)

        self.cache[(index, m, n)] = result
        
        return result