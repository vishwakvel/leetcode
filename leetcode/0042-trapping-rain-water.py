class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. Two pointer logic again, but this time we are updating the left_max and right_max to be used in the formula
        2. If left's height is less than right's, then we check if the height is greater than the max we have currently stored
            a) If it is greater, then we set the index's height as the new max and increase left by 1 (we can say theres no water at that index because if its height is greater than either max, that means that there can be no water there)
            b) If its less, then we can calculate the amount of water at that index because there's walls that have a greater height surrounding it
        3. Repeat for right but instead of increasing right you decrease by 1
        """
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
