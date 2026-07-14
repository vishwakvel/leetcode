class Solution:
    def rob(self, nums: List[int]) -> int:
        money = {}

        def dp(house):
            if house >= len(nums):
                return 0
            
            if house in money:
                return money[house]

            money[house] = max(nums[house] + dp(house + 2), dp(house + 1))

            return money[house]
        
        return dp(0)
