class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        1. Create a defaultdict to keep track of numbers we've already been through. The key is the number, and value is the last index they were seen at.
        2. Iterate through numbers and for each number check if it is in dict
            a) If it is, then check if it satisfies the condition (current index and last seen index, which is value in the dict, difference <= k, then True)
            b) If it isn't, continue
        3. Set dict's current num (key)'s value to current index
        4. If true hasn't been returned yet, no indices matched, so return False
        """
        seen = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
                
            seen[nums[i]] = i
        
        return False
