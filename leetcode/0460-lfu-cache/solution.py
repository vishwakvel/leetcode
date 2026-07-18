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
    
    def add(self, node):
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
    from collections import defaultdict

    def __init__(self, capacity: int):
        self.nodes = {} # key to node
        self.freq = defaultdict(DLL) # freq to dll of nodes of that freq (lru order)
        self.minFreq = 0
        self.capacity = capacity
    
    def update(self, node):
        freq = node.freq

        self.freq[freq].remove(node)

        if self.freq[freq].size == 0 and freq == self.minFreq:
            self.minFreq += 1
        
        node.freq += 1

        self.freq[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self.update(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.update(node)
            return
        
        if len(self.nodes) == self.capacity:
            lru = self.freq[self.minFreq].poplru()
            del self.nodes[lru.key]
        
        node = Node(key, value)
        self.nodes[key] = node
        self.minFreq = 1
        self.freq[self.minFreq].add(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
