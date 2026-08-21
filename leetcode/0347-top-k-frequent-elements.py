import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for i in range(len(nums) + 1)] # each index is freq

        for num, count in freq.items():
            buckets[count].append(num)

        ans = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
