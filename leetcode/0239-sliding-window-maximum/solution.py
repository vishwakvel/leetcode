class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        1. You want to keep track of the maxes using a deque, sorted from higheset to lowest.
        2. You move to the right all the way to the end of the list and first check if maxes isn't empty and if the index of the max for the previous window is less than the current index minus k
            a) If true, then it means that the max for the previous window is now outside the window since we moved to the right once
            b) If false, then continue 
        3. Then we go through and make sure the deque is sorted properly, so any numbers that are less than the new number we're about to add are removed from the deque since they're no longer needed
        4. Now we add the new index to the deque and finally check if the index is greater than k-1
            a) If it is, then that means we've finally reached the end of the first window so we can actually start adding to the ans list and start also moving past the window and change it.
            b) If it isn't, then continue
        """
        from collections import deque
        
        ans = []
        maxes = deque()

        for right in range(len(nums)):
            if maxes and maxes[0] < right - k + 1:
                maxes.popleft()
            
            while maxes and nums[maxes[-1]] < nums[right]:
                maxes.pop()
            
            maxes.append(right)

            if right >= k - 1:
                ans.append(nums[maxes[0]])
        
        return ans
