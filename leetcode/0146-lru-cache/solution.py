class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {} # key to node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])

        return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)

        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
