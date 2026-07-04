class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = ""
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                stack.append(int(num))
            elif s[i] == '[':
                stack.append('[')
                i += 1
            elif s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i] == ']':
                tmp = []
                while stack[-1] != '[':
                    tmp.append(stack.pop())
                tmp = "".join(tmp[::-1])
                stack.pop()
                num = stack.pop()
                res = ""
                for _ in range(num):
                    res += tmp
                stack.append(res)
                i += 1
        return "".join(stack)

            
            
            
