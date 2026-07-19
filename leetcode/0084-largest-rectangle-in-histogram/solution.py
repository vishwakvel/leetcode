class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][1] >= heights[i]:
                index, height = stack.pop()
                ans = max(ans, height*(i-index))
                start = index
            
            stack.append((start, heights[i]))
        
        for index, height in stack:
            ans = max(ans, height * (len(heights)-index))
        
        return ans
