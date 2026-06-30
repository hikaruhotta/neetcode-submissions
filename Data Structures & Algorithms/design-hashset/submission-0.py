class MyHashSet:

    def __init__(self):
        self.cache = [0] * 1000000
        

    def add(self, key: int) -> None:
        self.cache[key - 1] = 1

    def remove(self, key: int) -> None:
        self.cache[key - 1] = 0
        
    def contains(self, key: int) -> bool:
        return self.cache[key - 1] > 0
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)