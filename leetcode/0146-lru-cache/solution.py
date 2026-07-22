class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity
        self.hashmap = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
        
        node = Node(key, value)
        self.insert(node)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
