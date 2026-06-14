class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += ":"
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            # find number
            num = ""
            while s[i].isnumeric():
                num += s[i]
                i += 1

            num = int(num)
            
            # skip :
            i += 1

            # increment by number to grab string
            curr_s = s[i : i + num]
            result.append(curr_s)

            # update pointers
            i = i + num
        
        return result
