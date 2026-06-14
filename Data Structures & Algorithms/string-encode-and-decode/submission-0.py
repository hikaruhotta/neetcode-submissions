class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num_char = int(s[i:j])
            s_unit = s[j + 1 : j + 1 + num_char]
            result.append(s_unit)
            i = j + 1 + num_char
        
        return result
