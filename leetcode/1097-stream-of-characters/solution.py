class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.stream = []
        self.root = TrieNode()
        self.maxlen = max(len(word) for word in words)

        for word in words:
            curr = self.root

            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
            
            curr.isEnd = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        curr = self.root

        if len(self.stream) > self.maxlen:
            self.stream.pop(0)

        for char in reversed(self.stream):
            if char not in curr.children:
                return False
            
            curr = curr.children[char]

            if curr.isEnd:
                return True

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
