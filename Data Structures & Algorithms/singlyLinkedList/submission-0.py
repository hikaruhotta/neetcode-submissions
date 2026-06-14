class LinkedList:
    
    def __init__(self):
        self.arr = []
    
    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return -1
        return self.arr[index]
        
    def insertHead(self, val: int) -> None:
        self.arr = [val] + self.arr
        
    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.arr):
            return False

        before = self.arr[:index]
        if index + 1 < len(self.arr):
            after = self.arr[index + 1:]
        else:
            after = []
        self.arr = before + after
        return True


    def getValues(self) -> List[int]:
        return self.arr
        
