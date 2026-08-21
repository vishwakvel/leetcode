class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.hashmap = {} # key to bucket
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, bucket):
        prev = bucket.prev
        nxt = bucket.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, bucket, prev):
        nxt = prev.next

        bucket.prev = prev
        bucket.next = nxt

        nxt.prev = bucket
        prev.next = bucket

    def inc(self, key: str) -> None:
        if key not in self.hashmap:
            if self.head.next != self.tail and self.head.next.count == 1: # bucket 1
                bucket = self.head.next
            else:
                bucket = Bucket(1)
                self.insert(bucket, self.head)
        
            bucket.keys.add(key)
            self.hashmap[key] = bucket
        else:
            curr = self.hashmap[key]
            nxtcount = curr.count + 1

            if curr.next != self.tail and curr.next.count == nxtcount:
                nxt = curr.next
            else:
                nxt = Bucket(nxtcount)
                self.insert(nxt, curr)
            
            nxt.keys.add(key)
            self.hashmap[key] = nxt

            curr.keys.remove(key)
            
            if not curr.keys:
                self.remove(curr) # remove bucket if no keys left

    def dec(self, key: str) -> None:
        curr = self.hashmap[key]
        curr.keys.remove(key)

        if curr.count == 1: # delete key
            del self.hashmap[key]
        else:
            prevcount = curr.count - 1

            if curr.prev != self.head and curr.prev.count == prevcount:
                prev = curr.prev
            else:
                prev = Bucket(prevcount)
                self.insert(prev, curr.prev)
            
            prev.keys.add(key)
            self.hashmap[key] = prev
        
        if not curr.keys:
            self.remove(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        else:
            ans = self.tail.prev.keys.pop()
            self.tail.prev.keys.add(ans)
            return ans

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        else:
            ans = self.head.next.keys.pop()
            self.head.next.keys.add(ans)
            return ans


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
