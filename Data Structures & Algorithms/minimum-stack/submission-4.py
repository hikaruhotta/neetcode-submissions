class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = [] # (val, min at time of push)

    def push(self, val: int) -> None:
        self.stack.append((val, self.minimum))
        if self.minimum is None:
            self.minimum = val
        else:
            self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        (val, min_at_push) = self.stack.pop()
        self.minimum = min_at_push

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.minimum
