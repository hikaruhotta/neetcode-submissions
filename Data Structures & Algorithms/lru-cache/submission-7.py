class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first = ListNode(-1000, -1000)
        self.last = ListNode(-10000, -10000)
        self.first.next = self.last
        self.last.prev = self.first
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.append(node)

        self.print()
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.append(node)
            return

        while len(self.cache) + 1 > self.capacity:
            node_remove = self.first.next
            self.remove(node_remove)
            del self.cache[node_remove.key]
        
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.append(new_node)

        self.print()

    def remove(self, node: ListNode) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def append(self, node: ListNode) -> None:
        last_real_node = self.last.prev
        last_real_node.next, node.prev = node, last_real_node

        node.next, self.last.prev = self.last, node

    def print(self):
        curr = self.first

        result = []

        while curr:
            result.append((curr.key, curr.val))
            curr = curr.next
        
        print(result, self.cache)

