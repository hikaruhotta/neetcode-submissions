class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.matchsticks = sorted(matchsticks, reverse=True)
        return self.helper([0, 0, 0, 0], 0)

    def helper(self, path: List[int], index: int) -> bool:
        if index == len(self.matchsticks):
            return all([side == sum(self.matchsticks) // 4 for side in path])
        
        initial_side_lengths = set()
        for i in range(len(path)):
            if path[i] not in initial_side_lengths and path[i] + self.matchsticks[index] <= sum(self.matchsticks) // 4:
                initial_side_lengths.add(path[i])
                path[i] += self.matchsticks[index]
                if self.helper(path, index + 1):
                    return True
                path[i] -= self.matchsticks[index]
        
        return False
