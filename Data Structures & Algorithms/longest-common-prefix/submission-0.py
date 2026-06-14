class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]

            common_prefix = ""

            for i in range(min(len(result), len(s))):
                if result[i] == s[i]:
                    common_prefix += s[i]
                else:
                    break
            
            result = common_prefix
    
        return result