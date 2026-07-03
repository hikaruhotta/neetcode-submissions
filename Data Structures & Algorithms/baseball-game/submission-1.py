class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op[0] == '-' or op.isnumeric():
                if op[0] == '-':
                    stack.append(-int(op[1:]))
                else:
                    stack.append(int(op))
            elif op == '+':
                score1, score2 = stack[-1], stack[-2]
                stack.append(score1 + score2)
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()

        print(stack)
        
        return sum(stack)
                