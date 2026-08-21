class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        least = nums[0]
        most = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            oldmost = most
            oldleast = least

            most = max(x, x*oldmost, x*oldleast)
            least = min(x, x*oldleast, x*oldmost)

            ans = max(ans, most)
        
        return ans
