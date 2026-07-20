class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        # we want nums1 to be smaller
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left = 0
        right = m
        half = (m+n+1) // 2

        # binary search to find splitting point
        while left <= right:
            i = (left + right) // 2 # splitting point for nums1
            j = half - i # splitting point for nums2

            left1 = float("-inf") if i == 0 else nums1[i-1]
            right1 = float("inf") if i == m else nums1[i]
            left2 = float("-inf") if j == 0 else nums2[j-1]
            right2 = float("inf") if j == n else nums2[j]

            if left2 <= right1 and left1 <= right2:
                if (m+n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
