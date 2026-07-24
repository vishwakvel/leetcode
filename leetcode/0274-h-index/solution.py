class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for index, value in enumerate(citations):
            if n - index <= value:
                return n - index
        
        return 0
