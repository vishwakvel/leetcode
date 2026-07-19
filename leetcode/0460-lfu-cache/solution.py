from collections import defaultdict

class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

        self.size += 1
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1
    
    def poplru(self):
        if self.size == 0:
            return None

        lru = self.tail.prev
        self.remove(lru)
        return lru

class LFUCache:
    def __init__(self, capacity: int):
        self.hashmap = {} # key to node
        self.freq = defaultdict(DLL) # freq to dll
        self.capacity = capacity
        self.minFreq = 0
    
    def update(self, node):
        freq = node.freq

        self.freq[freq].remove(node)

        if freq == self.minFreq and self.freq[freq].size == 0:
            self.minFreq += 1
        
        freq += 1
        node.freq = freq
        self.freq[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.update(node)
            return
        
        node = Node(key, value)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            lru = self.freq[self.minFreq].poplru()
            del self.hashmap[lru.key]
        
        self.minFreq = 1
        self.freq[1].insert(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
