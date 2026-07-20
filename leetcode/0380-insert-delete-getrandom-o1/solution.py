import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        self.array.append(val)
        self.hashmap[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        
        index = self.hashmap[val]
        self.array[-1], self.array[index] = self.array[index], self.array[-1]
        self.hashmap[self.array[index]] = index
        self.array.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
