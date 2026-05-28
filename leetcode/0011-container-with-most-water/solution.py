class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. Two pointer logic again, so first set up left to be 0 and right to be end of list, as well as area to be 0 by default
        2. Calculate the area by doing the max of the current area's value and the new calculation (which is min of heights * width)
        3. Check if left height is less than right height
            a) If it is, left += 1 (increase left)
            b) If it isn't, right -= 1 (decrease right)
        """
        area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
