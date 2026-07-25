import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0)) # add all possibilities with all nums1 and only first num in nums2

        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)

            ans.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1)) # add next num in nums2 if theres space

        return ans
