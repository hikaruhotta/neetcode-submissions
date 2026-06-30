class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result

        for i in range(min([len(s) for s in strs])):
            if all(s[i] == strs[0][i] for s in strs):
                result += strs[0][i]
            else:
                break
        
        return result