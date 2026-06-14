class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numbers = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                num2 = numbers.pop()
                num1 = numbers.pop()
                if token == '+':
                    numbers.append(num1 + num2)
                elif token == '-':
                    numbers.append(num1 - num2)
                elif token == '*':
                    numbers.append(num1 * num2)
                elif token == '/':
                    numbers.append(int(float(num1) / num2))
            else:
                numbers.append(int(token))
        
        return numbers[0]
