class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1. Create empty stack and set area equal to 0
        2. For each height in the list, we set start equal to that index, then we check if the stack isn't empty and if the last element of the stack has a height greater than the current index's height
            a) If both statements are true, then you pop the stack and compute the area and set area equal to the max of the previous max and the current area. Also you set start equal to the index of the popped height's index since the new height that was added is greater, so the index for width can start before. Repeat this until either statement isn't true
            b) If either isn't true, continue
        3. Add the current element's height to the stack along with the start (can either be the current index or the leftmost index of a height thats smaller and allows for a proper horizontal rectangle)
        4. After going through the whole stack once, process the leftovers in the stack by computing the areas of each from the end to wherever the start is set at and change area based on whatever is the greatest.
        """
        stack = []
        area = 0

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][-1] > heights[i]:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            
            stack.append((start, heights[i]))
        
        for index, height in stack:
            area = max(area, height * (len(heights) - index))
        
        return area
