class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        size = valueDiff + 1
        hashmap = {} # bucket to num

        for i in range(len(nums)):
            num = nums[i]
            bucket = num // size

            if bucket in hashmap:
                return True
            
            if bucket - 1 in hashmap and abs(num - hashmap[bucket-1]) <= valueDiff:
                return True
            
            if bucket + 1 in hashmap and abs(num - hashmap[bucket+1]) <= valueDiff:
                return True
            
            hashmap[bucket] = num

            if i >= indexDiff:
                left = nums[i - indexDiff]
                del hashmap[left // size]
        
        return False
