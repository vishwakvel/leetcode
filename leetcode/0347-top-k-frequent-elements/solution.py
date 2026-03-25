class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        
        numsdict = {}

        for num in nums: # making a dict with key = num and value = count
            numsdict[num] = 1 + numsdict.get(num, 0)
        
        sorted_numsdict = dict(sorted(numsdict.items(), key=lambda item: item[1], reverse = True)) # sorting the dict based on freq in descending order so most freq at the beginning

        return list(sorted_numsdict.keys())[:k] # returning first k keys which represent top k frequent elements
