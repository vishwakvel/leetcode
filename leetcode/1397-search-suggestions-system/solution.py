class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        for product in sorted(products):
            node = root

            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                
                node = node.children[char]

                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        
        ans = []
        node = root

        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                ans.append(node.suggestions)
            else:
                node = None
                ans.append([])
        
        return ans
