from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        visiting = set(wordList)

        if endWord not in visiting:
            return []
        
        parents = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        
        while queue:
            word = queue.popleft()

            if word == endWord:
                break
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]

                    if newWord not in visiting:
                        continue

                    if newWord not in distance:
                        distance[newWord] = distance[word] + 1
                        parents[newWord].append(word)
                        queue.append(newWord)
                    elif distance[newWord] == distance[word] + 1:
                        parents[newWord].append(word)
                    
        if endWord not in distance:
            return []
        
        ans = []

        def backtracking(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return
            
            for parent in parents[word]:
                path.append(parent)
                backtracking(parent, path)
                path.pop()
        
        backtracking(endWord, [endWord])
        return ans
