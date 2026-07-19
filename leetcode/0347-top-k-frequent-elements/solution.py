import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        heap = []

        for num in nums:
            hashmap[num] += 1
        
        for num in hashmap:
            heapq.heappush(heap, (hashmap[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [element for freq, element in heap]
