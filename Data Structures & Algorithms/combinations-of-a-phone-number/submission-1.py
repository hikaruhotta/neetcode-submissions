class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        self.results = []
        self.helper(digits, "")
        return self.results
    
    def helper(self, digits: str, seq: str) -> None:
        if len(digits) == 0:
            self.results.append(seq)
            return
        
        for candidate in self.letterCandidates(int(digits[0])):
            seq += candidate
            self.helper(digits[1:], seq)
            seq = seq[:-1]
        
    def letterCandidates(self, digit: int) -> List[str]:
        candidates = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        return candidates[digit]