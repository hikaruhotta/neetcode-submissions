class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.results = []
        self.helper(0, [], target)
        return self.results
    
    def helper(self, index: int, seq: List[int], target: int) -> None:
        if target == 0:
            self.results.append(seq.copy())
        if index == len(self.candidates):
            return
        
        for i in range(index, len(self.candidates)):
            if i > index and self.candidates[i] == self.candidates[i - 1]:
                continue
            
            if self.candidates[i] <= target:
                seq.append(self.candidates[i])
                self.helper(i + 1, seq, target - self.candidates[i])
                seq.pop()
        