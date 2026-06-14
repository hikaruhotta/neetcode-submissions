class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            c_map = [0] * 26
            for c in s:
                c_map[ord(c) - ord('a')] += 1
            if tuple(c_map) in result:
                result[tuple(c_map)].append(s)
            else:
                result[tuple(c_map)] = [s]
        
        return [value for _, value in result.items()]