from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            encoding = self.encode(s)
            if encoding not in groups:
                groups[encoding] = []
            groups[encoding].append(s)
        
        return [group for group in groups.values()]

    def encode(self, s: str) -> tuple:
        encoding = [0] * 26
        for ch in s:
            key = ord(ch) - ord('a')
            encoding[key] += 1
        return tuple(encoding)