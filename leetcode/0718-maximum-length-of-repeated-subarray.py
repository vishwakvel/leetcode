class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for i in range(len(nums1))]
        ans = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                    
                    ans = max(ans, dp[i][j])
        
        return ans
