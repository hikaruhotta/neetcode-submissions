class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_index = 0
        self.stack.append((val, self.min_index))
        min_value, _ = self.stack[self.min_index]
        if val < min_value:
            self.min_index = len(self.stack) - 1

    def pop(self) -> None:
        if self.min_index == len(self.stack) - 1:
            self.min_index = self.stack[-1][1]
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[self.min_index][0]
        
