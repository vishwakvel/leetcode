class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        m = len(board)
        n = len(board[0])

        for word in words:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
            
            curr.isEnd = True
        
        ans = set()
        
        def backtracking(r, c, node, path):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            
            char = board[r][c]

            if char == "#" or char not in node.children:
                return
            
            node = node.children[char]
            path += char
            
            if node.isEnd:
                ans.add(path)
            
            board[r][c] = "#"

            backtracking(r + 1, c, node, path)
            backtracking(r - 1, c, node, path)
            backtracking(r, c + 1, node, path)
            backtracking(r, c - 1, node, path)

            board[r][c] = char
        
        for r in range(m):
            for c in range(n):
                backtracking(r, c, root, "")
        
        return list(ans)
