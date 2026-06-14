class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distances = [(x**2 + y**2, [x,y]) for x,y in points]
        heapq.heapify(distances)

        while k:
            closest = heapq.heappop(distances)[1]
            ans.append(closest)
            k -= 1
        
        return ans
