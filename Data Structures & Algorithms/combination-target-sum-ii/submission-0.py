class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.curr = []
        self.result = []
        self.dfs(0, target)
        return self.result

    def dfs(self, index, target):
        if target == 0:
            self.result.append(self.curr.copy())
            return
        elif index >= len(self.candidates):
            return
        
        prev_candidate = None
        for i in range(index, len(self.candidates)):
            candidate = self.candidates[i]
            if candidate is not prev_candidate and candidate <= target:
                self.curr.append(candidate)
                self.dfs(i + 1, target - candidate)
                self.curr.pop()
            prev_candidate = candidate
        
