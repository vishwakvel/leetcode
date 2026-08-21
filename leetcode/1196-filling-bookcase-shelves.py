class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # each state represents height needed to place first i books
        dp = [float("inf")] * (len(books) + 1)
        dp[0] = 0

        for i in range(len(books)):
            width = 0
            maxheight = 0

            for j in range(i, len(books)):
                thickness, height = books[j]

                if width + thickness > shelfWidth:
                    break
                
                width += thickness
                maxheight = max(maxheight, height)
                dp[j+1] = min(dp[j+1], dp[i] + maxheight)
        
        return dp[-1]
