class MinStack:

    def __init__(self):
        self.min_value = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_value))
        if self.min_value is None:
            self.min_value = val
        else:
            self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        val, prev_min_value = self.stack.pop()
        self.min_value = prev_min_value

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_value
        
