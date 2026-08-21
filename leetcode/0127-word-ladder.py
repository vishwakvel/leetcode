from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set(wordList)
        
        if endWord not in visited:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new = word[:i] + char + word[i+1:]

                    if new in visited:
                        visited.remove(new)
                        queue.append((new, steps+1))
            
        return 0
