class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif len(token) >= 2 and token[0] == '-' and token[1:].isnumeric():
                stack.append(-int(token[1:]))
            elif token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                
                stack.append(result)
        
        return stack[0]

