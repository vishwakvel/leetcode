class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()

        for word in wordDict:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
            
            curr.isEnd = True
        
        memo = {}
        
        def dp(index):
            if index == len(s):
                return True
            
            if index in memo:
                return memo[index]
            
            curr = root
            
            for i in range(index, len(s)):
                char = s[i]

                if char not in curr.children:
                    break
                
                curr = curr.children[char]

                if curr.isEnd:
                    if dp(i + 1):
                        memo[index] = True
                        return True
        
            memo[index] = False
            return False
        
        return dp(0)
