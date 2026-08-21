import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        heap = []

        for x, y in points:
            dist = x*x + y*y

            heapq.heappush(heap, (-dist, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]
        """
        import random

        def dist(point):
            return point[0] * point[0] + point[1] * point[1]

        def partition(left, right):
            index = random.randint(left, right)
            points[index], points[right] = points[right], points[index]
            pivotdist = dist(points[right])
            store = left

            for i in range(left, right):
                if dist(points[i]) < pivotdist:
                    points[store], points[i] = points[i], points[store]
                    store += 1
            
            points[store], points[right] = points[right], points[store]
            return store
        
        left = 0
        right = len(points) - 1

        while left <= right:
            index = partition(left, right)

            if index == k:
                break
            elif index < k:
                left = index + 1
            else:
                right = index - 1
        
        return points[:k]
