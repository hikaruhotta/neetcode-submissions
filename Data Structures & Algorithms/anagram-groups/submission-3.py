from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i, s in enumerate(strs):
            encoding = self.encode(s)
            if encoding not in groups:
                groups[encoding] = []
            groups[encoding].append(i)
        
        return [[strs[i] for i in group] for group in groups.values()]

    def encode(self, s: str) -> tuple:
        encoding = [0] * 26
        for ch in s:
            key = ord(ch) - ord('a')
            encoding[key] += 1
        return tuple(encoding)