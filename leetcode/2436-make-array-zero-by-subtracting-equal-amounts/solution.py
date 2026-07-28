class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsset = set(nums)
        
        if 0 in numsset:
            return len(numsset)-1
        else:
            return len(numsset)
