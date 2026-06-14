class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertRight(node)
            return node.val
        
        return -1

    def insertRight(self, node) -> None:
        right_prev = self.right.prev
        right_prev.next, node.prev = node, right_prev
        node.next, self.right.prev = self.right, node

    def removeLeft(self) -> Optional[Node]:
        left_next = self.left.next
        if left_next != self.right:
            left_next_next = left_next.next
            self.left.next, left_next_next.prev = left_next_next, self.left
            return left_next

        return None
    
    def remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insertRight(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insertRight(node)
        
        while len(self.cache) > self.capacity:
            node = self.removeLeft()
            del self.cache[node.key]
            
            
        
