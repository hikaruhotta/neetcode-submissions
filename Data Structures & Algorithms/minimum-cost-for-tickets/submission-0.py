class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.costs = costs
        self.days = days

        self.cache = {}

        return self.helper(0)
    
    def helper(self, index):
        if index == len(self.days):
            return 0

        if index in self.cache:
            return self.cache[index]
        
        one_day = self.costs[0] + self.helper(index + 1)

        i = index
        while i < len(self.days) and self.days[i] <= self.days[index] + 6:
            i += 1
        seven_day = self.costs[1] + self.helper(i)

        i = index
        while i < len(self.days) and self.days[i] <= self.days[index] + 29:
            i += 1
        thirty_day = self.costs[2] + self.helper(i)

        result = min(one_day, seven_day, thirty_day)

        self.cache[index] = result

        return result



