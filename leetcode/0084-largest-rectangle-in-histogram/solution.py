class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for index in range(len(heights) + 1):
            curr = 0 if index == len(heights) else heights[index]

            while stack and heights[stack[-1]] > curr:
                height = heights[stack.pop()]

                if not stack:
                    width = index
                else:
                    width = index - stack[-1] - 1
                
                ans = max(ans, height * width)
            
            stack.append(index)
        
        return ans
