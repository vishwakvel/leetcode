class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        counts = [0] * 100
        largest = nums[0]
        smallest = nums[0]
        ans = []

        for num in nums:
            counts[num-1] = 1

            largest = max(largest, num)
            smallest = min(smallest, num)

        for i in range(smallest, largest+1):
            if not counts[i-1]:
                ans.append(i)
        
        return ans