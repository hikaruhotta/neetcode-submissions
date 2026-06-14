class ListNode:

    def __init__(self, key: int, value: int, prev: Optional[ListNode], next: Optional[ListNode]):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.numNodes = 0
        self.cache = {}

        self.falseHead = ListNode(0, 0, None, None)
        self.falseTail = ListNode(0, 0, None, None)

        self.falseHead.next = self.falseTail
        self.falseTail.prev = self.falseHead

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.insertNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.insertNode(node)
        else:
            newNode = ListNode(key, value, None, None)
            self.cache[key] = newNode
            self.insertNode(newNode)
        
        if len(self.cache) > self.capacity:
            toRemoveNode = self.falseHead.next
            del self.cache[toRemoveNode.key]
            self.removeNode(toRemoveNode)


    def insertNode(self, node: ListNode):
        prevNode = self.falseTail.prev

        prevNode.next = node
        node.prev = prevNode

        self.falseTail.prev = node
        node.next = self.falseTail
        

    def removeNode(self, node: ListNode):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        

    




        
